"""
DhwaniLekh (ध्वनिलेख)
Fast, local-first, privacy-focused open-source speech-to-text dictation.
"""

__version__ = "0.1.0"
__author__ = "DhwaniLekh Contributors"

from dhwanilekh.cleaner import TextCleaner
from dhwanilekh.config import Config


def get_app(*args, **kwargs):
    """Lazy loader for DhwaniLekhApp to avoid importing heavy dependencies at module load time."""
    from dhwanilekh.app import DhwaniLekhApp
    return DhwaniLekhApp(*args, **kwargs)


__all__ = ["get_app", "Config", "TextCleaner", "__version__"]
