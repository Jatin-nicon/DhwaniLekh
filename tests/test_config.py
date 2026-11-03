"""
Unit tests for Config management.
"""

from pathlib import Path
import tempfile
import unittest

from dhwanilekh.config import Config


class TestConfig(unittest.TestCase):
    def test_default_values(self):
        cfg = Config()
        self.assertEqual(cfg.hotkey, "ctrl+space")
        self.assertEqual(cfg.model_size, "base")
        self.assertEqual(cfg.compute_type, "int8")
        self.assertEqual(cfg.sample_rate, 16000)
        self.assertEqual(cfg.language, "en")
        self.assertEqual(cfg.paste_mode, "clipboard")
        self.assertTrue(cfg.speak_status)

    def test_from_dict_and_to_dict(self):
        custom = {
            "hotkey": "alt+d",
            "model_size": "small",
            "language": "hi",
            "speak_status": False,
        }
        cfg = Config.from_dict(custom)
        self.assertEqual(cfg.hotkey, "alt+d")
        self.assertEqual(cfg.model_size, "small")
        self.assertEqual(cfg.language, "hi")
        self.assertFalse(cfg.speak_status)
        self.assertEqual(cfg.paste_mode, "clipboard")

        data = cfg.to_dict()
        self.assertEqual(data["hotkey"], "alt+d")
        self.assertEqual(data["language"], "hi")

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "test_settings.json"
            cfg = Config(hotkey="ctrl+shift+v", model_size="tiny")
            cfg.save(file_path)

            self.assertTrue(file_path.exists())
            loaded = Config.load(file_path)
            self.assertEqual(loaded.hotkey, "ctrl+shift+v")
            self.assertEqual(loaded.model_size, "tiny")


if __name__ == "__main__":
    unittest.main()

