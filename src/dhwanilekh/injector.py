"""
Text injection into active applications via clipboard or keystroke simulation.
"""

import time
import pyautogui
import pyperclip


class TextInjector:
    """Injects text into the currently active desktop window."""

    def __init__(self, mode: str = "clipboard"):
        self.mode = mode
        pyautogui.FAILSAFE = True

    def inject(self, text: str) -> None:
        """Inject text into active window using the configured mode."""
        if not text:
            return

        if self.mode == "typing":
            pyautogui.write(text, interval=0.01)
        else:
            # Clipboard paste (default, fastest, supports Unicode/multilingual)
            pyperclip.copy(text)
            time.sleep(0.05)
            pyautogui.hotkey("ctrl", "v")
