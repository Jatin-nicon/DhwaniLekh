"""
Speech transcription engine for DhwaniLekh using faster-whisper.
"""

from pathlib import Path
from typing import Callable, Optional

from faster_whisper import WhisperModel


class Transcriber:
    """Manages speech-to-text inference with faster-whisper."""

    def __init__(
        self,
        model_size: str = "base",
        compute_type: str = "int8",
        device: str = "cpu",
        language: Optional[str] = "en",
        on_status: Optional[Callable[[str], None]] = None,
    ):
        self.model_size = model_size
        self.compute_type = compute_type
        self.device = device
        self.language = language
        self.on_status = on_status or (lambda msg: None)
        self._model: Optional[WhisperModel] = None

    def ensure_model(self) -> WhisperModel:
        """Lazily load the Whisper model upon first transcription request."""
        if self._model is None:
            self.on_status("Loading transcription model...")
            self._model = WhisperModel(
                self.model_size,
                device=self.device,
                compute_type=self.compute_type,
            )
            self.on_status("Model loaded.")
        return self._model

    def transcribe(self, audio_path: Path) -> str:
        """Transcribe an audio file and return the combined text."""
        model = self.ensure_model()
        segments, _ = model.transcribe(
            str(audio_path),
            language=self.language,
            vad_filter=True,
            beam_size=1,
        )
        return " ".join(segment.text.strip() for segment in segments).strip()

