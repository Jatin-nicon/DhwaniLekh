# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Standard open-source project structure with `src/dhwanilekh/` package layout.
- Modular subsystems for audio recording, transcription, text cleanup, injection, and feedback.
- Automated test suite for text cleanup and configuration validation.
- GitHub Actions CI workflow for multi-version Python testing and linting.
- Open-source community guidelines, issue templates, PR template, Code of Conduct, and Contributing guides.
- Modern `pyproject.toml` supporting `pip install -e .`.

---

## [0.1.0] - 2026-11-03

### Added
- Initial MVP release of DhwaniLekh.
- Global hotkey toggle (default `Ctrl+Space`) to start and stop audio capture.
- Local transcription pipeline using `faster-whisper`.
- Audio capture via `sounddevice` with automatic temporary WAV persistence.
- Basic spoken punctuation commands (e.g., "comma", "period", "question mark", "new line").
- Automatic clipboard paste and typing injection into active desktop applications.
- Text-to-speech audio status feedback via `pyttsx3`.
- Configuration persistence with `settings.json`.

