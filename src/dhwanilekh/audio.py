"""
Microphone audio capture manager for DhwaniLekh.
"""

from pathlib import Path
import queue
import tempfile
import threading
from typing import List, Optional

import numpy as np
import sounddevice as sd
import soundfile as sf


class AudioRecorder:
    """Manages recording audio from the microphone via sounddevice."""

    def __init__(self, sample_rate: int = 16000, channels: int = 1):
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio_queue: queue.Queue = queue.Queue()
        self.audio_frames: List[np.ndarray] = []
        self.is_recording: bool = False
        self._thread: Optional[threading.Thread] = None
        self.temp_audio_path = Path(tempfile.gettempdir()) / "dhwanilekh_recording.wav"

    def _callback(self, indata: np.ndarray, frames: int, time_info: dict, status: sd.CallbackFlags) -> None:
        if status:
            print(f"[Audio Status] {status}")
        self.audio_queue.put(indata.copy())

    def start(self) -> None:
        """Start capturing audio in a background thread."""
        if self.is_recording:
            return

        self.is_recording = True
        self.audio_frames = []

        # Flush any leftover chunks in queue
        while not self.audio_queue.empty():
            try:
                self.audio_queue.get_nowait()
            except queue.Empty:
                break

        self._thread = threading.Thread(target=self._record_loop, daemon=True)
        self._thread.start()

    def _record_loop(self) -> None:
        try:
            with sd.InputStream(
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype="float32",
                callback=self._callback,
            ):
                while self.is_recording:
                    try:
                        chunk = self.audio_queue.get(timeout=0.25)
                        self.audio_frames.append(chunk)
                    except queue.Empty:
                        continue
        except Exception as e:
            print(f"[Audio Error] Failed to open audio input stream: {e}")
            self.is_recording = False

    def stop(self) -> Optional[Path]:
        """Stop recording and return the saved temporary WAV file path."""
        if not self.is_recording:
            return None

        self.is_recording = False
        if self._thread:
            self._thread.join(timeout=2.0)

        if not self.audio_frames:
            return None

        audio = np.concatenate(self.audio_frames, axis=0)
        sf.write(str(self.temp_audio_path), audio, self.sample_rate)
        return self.temp_audio_path

