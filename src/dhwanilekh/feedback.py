"""
Audio and spoken feedback engine for DhwaniLekh.
"""

from typing import Optional


class FeedbackService:
    """Provides audio/TTS status announcements."""

    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        self._engine = None
        if self.enabled:
            self._init_tts()

    def _init_tts(self) -> None:
        try:
            import pyttsx3
            self._engine = pyttsx3.init()
            self._engine.setProperty("rate", 190)
            self._engine.setProperty("volume", 1.0)
            # Prefer clear voice if available
            for voice in self._engine.getProperty("voices"):
                name = (voice.name or "").lower()
                if "hazel" in name or "zira" in name or "female" in name:
                    self._engine.setProperty("voice", voice.id)
                    break
        except Exception:
            self._engine = None

    def announce(self, message: str) -> None:
        """Announce status message via console and optional TTS."""
        print(f"[DhwaniLekh] {message}")
        if self.enabled and self._engine:
            try:
                self._engine.say(message)
                self._engine.runAndWait()
            except Exception:
                pass

