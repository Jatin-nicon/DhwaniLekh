"""
Unit tests for TextCleaner.
"""

import unittest
from dhwanilekh.cleaner import TextCleaner


class TestTextCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = TextCleaner()

    def test_empty_string(self):
        self.assertEqual(self.cleaner.clean(""), "")
        self.assertEqual(self.cleaner.clean("   "), "")

    def test_spoken_punctuation_replacement(self):
        sample = "hello comma how are you question mark"
        result = self.cleaner.clean(sample)
        self.assertEqual(result, "Hello, how are you?")

    def test_spoken_full_stop_and_period(self):
        sample1 = "this is sentence one full stop this is sentence two period"
        result1 = self.cleaner.clean(sample1)
        self.assertEqual(result1, "This is sentence one. This is sentence two.")

    def test_spoken_newline(self):
        sample = "dear team comma new line please review this report period"
        result = self.cleaner.clean(sample)
        self.assertIn("\n", result)
        self.assertTrue(result.startswith("Dear team,\n"))

    def test_capitalization(self):
        sample = "this is lowercase"
        result = self.cleaner.clean(sample)
        self.assertTrue(result.startswith("This"))
        self.assertTrue(result.endswith("."))

    def test_preserve_existing_punctuation(self):
        sample = "Is this already punctuated?"
        result = self.cleaner.clean(sample)
        self.assertEqual(result, "Is this already punctuated?")


if __name__ == "__main__":
    unittest.main()

