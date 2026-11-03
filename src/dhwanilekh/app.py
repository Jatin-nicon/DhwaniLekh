"""
Main application coordinator for DhwaniLekh.
"""

from pathlib import Path
import time
from typing import Optional

import keyboard

from dhwanilekh.audio import AudioRecorder
from dhwanilekh.cleaner import TextCleaner
from dhwanilekh.config import Config
from dhwanilekh.feedback import FeedbackService
from dhwanilekh.injector import TextInjector
from dhwanilekh.transcriber import Transcriber


class DhwaniLekhApp:
    """Coordinates hotkey listeners, recording, transcription, and typing."""

    def __init__(self, config_path: Optional[Path] = None):
        self.config = Config.load(config_path)
        self.feedback = FeedbackService(enabled=self.config.speak_status)
        self.audio = AudioRecorder(sample_rate=self.config.sample_rate)
        self.cleaner = TextCleaner()
        self.injector = TextInjector(mode=self.config.paste_mode)
        self.transcriber = Transcriber(
            model_size=self.config.model_size,
            compute_type=self.config.compute_type,
            language=self.config.language,
            on_status=self.feedback.announce,
        )
        self.running = False

    def toggle_recording(self) -> None:
        """Toggle audio recording on and off."""
        if self.audio.is_recording:
            self.stop_and_process()
        else:
            self.start_recording()

    def start_recording(self) -> None:
        """Begin audio capture."""
        self.feedback.announce("Recording started.")
        self.audio.start()

    def stop_and_process(self) -> None:
        """Stop capture, transcribe speech, format, and inject text."""
        self.feedback.announce("Transcribing...")
        audio_file = self.audio.stop()

        if not audio_file:
            self.feedback.announce("No audio captured.")
            return

        try:
            raw_text = self.transcriber.transcribe(audio_file)
            if not raw_text:
                self.feedback.announce("No speech detected.")
                return

            clean_text = self.cleaner.clean(raw_text)
            self.injector.inject(clean_text)
            self.feedback.announce("Done.")
        except Exception as e:
            self.feedback.announce(f"Error during transcription: {e}")

    def run(self) -> None:
        """Start listening for global hotkey and run the event loop."""
        self.running = True
        print("=" * 60)
        print("  DhwaniLekh (ध्वनिलेख) — Local Voice-to-Text Dictation")
        print("=" * 60)
        print(f"  • Global Hotkey : {self.config.hotkey}")
        print(f"  • Model Size    : {self.config.model_size}")
        print(f"  • Language      : {self.config.language or 'auto-detect'}")
        print(f"  • Paste Mode    : {self.config.paste_mode}")
        print("=" * 60)
        print("Press the hotkey to start recording, speak, then press it again to paste.")
        print("Press Ctrl+C in this terminal to exit.\n")

        self.feedback.announce("DhwaniLekh is ready.")
        keyboard.add_hotkey(self.config.hotkey, self.toggle_recording, suppress=False)

        try:
            while self.running:
                time.sleep(0.2)
        except KeyboardInterrupt:
            self.running = False
            self.feedback.announce("Stopping DhwaniLekh.")


def main() -> None:
    """CLI entrypoint."""
    app = DhwaniLekhApp()
    app.run()


if __name__ == "__main__":
    main()

