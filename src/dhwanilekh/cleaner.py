"""
Text normalization, spoken punctuation replacement, and formatting for DhwaniLekh.
"""

import re
from typing import Dict


class TextCleaner:
    """Cleans transcribed speech into properly formatted written text."""

    DEFAULT_REPLACEMENTS: Dict[str, str] = {
        r"\bnew line\b": "\n",
        r"\bnext line\b": "\n",
        r"\bnew paragraph\b": "\n\n",
        r"\bcomma\b": ",",
        r"\bfull stop\b": ".",
        r"\bperiod\b": ".",
        r"\bquestion mark\b": "?",
        r"\bexclamation mark\b": "!",
        r"\bcolon\b": ":",
        r"\bsemicolon\b": ";",
    }

    def __init__(self, spoken_punctuation: bool = True):
        self.spoken_punctuation = spoken_punctuation

    def clean(self, raw_text: str) -> str:
        """Process raw transcription output into formatted text."""
        if not raw_text or not raw_text.strip():
            return ""

        text = raw_text.strip()

        # Spoken punctuation replacements
        if self.spoken_punctuation:
            for pattern, replacement in self.DEFAULT_REPLACEMENTS.items():
                text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        # Normalize spaces before punctuation
        text = re.sub(r"\s+([,.:;?!])", r"\1", text)
        # Ensure single space after punctuation if followed by a character (except newlines or end of string)
        text = re.sub(r"([,.:;?!])(?=[^\s\d\n])", r"\1 ", text)

        # Clean spaces around newlines: strip trailing spaces before \n and leading spaces after \n
        text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)

        # Collapse multiple horizontal spaces to a single space
        text = re.sub(r"[^\S\r\n]+", " ", text)
        text = text.strip()

        # Capitalize first character of entire text
        if text and text[0].islower():
            text = text[0].upper() + text[1:]

        # Capitalize after sentence terminators (. ! ?)
        def capitalize_sentence(match: re.Match) -> str:
            return match.group(1) + match.group(2).upper()

        text = re.sub(r"([.!?]\s+)([a-z])", capitalize_sentence, text)

        # Capitalize at the start of any new line
        text = re.sub(r"(\n+)([a-z])", capitalize_sentence, text)

        # Ensure sentence has ending punctuation if it ends with alphanumeric
        if text and text[-1].isalnum():
            text += "."

        return text
