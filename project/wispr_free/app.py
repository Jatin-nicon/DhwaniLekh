import json
import queue
import tempfile
import threading
import time
from pathlib import Path

import keyboard
import numpy as np
import pyautogui
import pyperclip
import pyttsx3
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

pyautogui.FAILSAFE = True
BASE_DIR = Path(__file__).resolve().parent
SETTINGS_PATH = BASE_DIR / "settings.json"
TEMP_AUDIO_PATH = Path(tempfile.gettempdir()) / "wispr_free_recording.wav"

DEFAULT_SETTINGS = {
    "hotkey": "ctrl+space",
    "model_size": "base",
    "compute_type": "int8",
    "sample_rate": 16000,
    "language": "en",
    "paste_mode": "clipboard",
    "speak_status": True
}


class WisprFree:
    def __init__(self):
        self.settings = self.load_settings()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 190)
        self.engine.setProperty("volume", 1.0)
        self.set_female_voice_if_available()
        self.model = None
        self.is_recording = False
        self.audio_frames = []
        self.audio_queue = queue.Queue()
        self.recording_thread = None
        self.running = True

    def load_settings(self):
        if SETTINGS_PATH.exists():
            data = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
            merged = DEFAULT_SETTINGS.copy()
            merged.update(data)
            return merged
        SETTINGS_PATH.write_text(json.dumps(DEFAULT_SETTINGS, indent=2), encoding="utf-8")
        return DEFAULT_SETTINGS.copy()

    def set_female_voice_if_available(self):
        try:
            for voice in self.engine.getProperty("voices"):
                name = (voice.name or "").lower()
                if "hazel" in name or "zira" in name or "female" in name:
                    self.engine.setProperty("voice", voice.id)
                    return
        except Exception:
            pass

    def say(self, text):
        print(f"[WisprFree] {text}")
        if self.settings.get("speak_status", True):
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass

    def ensure_model(self):
        if self.model is None:
            self.say("Loading transcription model. First start may take a moment.")
            self.model = WhisperModel(
                self.settings["model_size"],
                device="cpu",
                compute_type=self.settings["compute_type"],
            )
            self.say("Model loaded.")

    def audio_callback(self, indata, frames, time_info, status):
        if status:
            print(status)
        self.audio_queue.put(indata.copy())

    def start_recording(self):
        if self.is_recording:
            return
        self.is_recording = True
        self.audio_frames = []
        while not self.audio_queue.empty():
            try:
                self.audio_queue.get_nowait()
            except queue.Empty:
                break
        self.say("Recording started.")
        self.recording_thread = threading.Thread(target=self._record_loop, daemon=True)
        self.recording_thread.start()

    def _record_loop(self):
        samplerate = self.settings["sample_rate"]
        with sd.InputStream(samplerate=samplerate, channels=1, dtype="float32", callback=self.audio_callback):
            while self.is_recording:
                try:
                    chunk = self.audio_queue.get(timeout=0.25)
                    self.audio_frames.append(chunk)
                except queue.Empty:
                    continue

    def stop_recording(self):
        if not self.is_recording:
            return
        self.is_recording = False
        if self.recording_thread:
            self.recording_thread.join(timeout=2)
        if not self.audio_frames:
            self.say("No audio captured.")
            return
        self.say("Transcribing.")
        audio = np.concatenate(self.audio_frames, axis=0)
        sf.write(str(TEMP_AUDIO_PATH), audio, self.settings["sample_rate"])
        text = self.transcribe(TEMP_AUDIO_PATH)
        if text:
            final_text = self.cleanup_text(text)
            self.insert_text(final_text)
            self.say("Done.")
        else:
            self.say("I did not catch any usable speech.")

    def transcribe(self, audio_path: Path):
        self.ensure_model()
        segments, info = self.model.transcribe(
            str(audio_path),
            language=self.settings.get("language") or None,
            vad_filter=True,
            beam_size=1,
        )
        text = " ".join(segment.text.strip() for segment in segments).strip()
        print(f"[Transcription] {text}")
        return text

    def cleanup_text(self, text: str):
        text = " ".join(text.split())
        replacements = {
            " new line ": "\n",
            " comma": ",",
            " full stop": ".",
            " period": ".",
            " question mark": "?",
            " exclamation mark": "!",
        }
        padded = f" {text} "
        for old, new in replacements.items():
            padded = padded.replace(old, new)
        text = padded.strip()
        if text and text[0].islower():
            text = text[0].upper() + text[1:]
        if text and text[-1].isalnum():
            text += "."
        return text

    def insert_text(self, text: str):
        print(f"[Output] {text}")
        if self.settings.get("paste_mode") == "typing":
            pyautogui.write(text, interval=0.01)
        else:
            pyperclip.copy(text)
            time.sleep(0.05)
            pyautogui.hotkey("ctrl", "v")

    def toggle_recording(self):
        if self.is_recording:
            self.stop_recording()
        else:
            self.start_recording()

    def run(self):
        print("WisprFree started.")
        print(f"Hotkey: {self.settings['hotkey']}")
        print("Press the hotkey once to start recording and again to stop and transcribe.")
        print("Press Ctrl+C in this console to quit.")
        self.say("Wispr Free is ready.")
        keyboard.add_hotkey(self.settings["hotkey"], self.toggle_recording, suppress=False)
        try:
            while self.running:
                time.sleep(0.2)
        except KeyboardInterrupt:
            self.running = False
            self.say("Stopping Wispr Free.")


if __name__ == "__main__":
    WisprFree().run()
