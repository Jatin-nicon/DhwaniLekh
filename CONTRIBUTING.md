# Contributing to DhwaniLekh (ध्वनिलेख)

First off, thank you for considering contributing to **DhwaniLekh**! 🎉

DhwaniLekh is an open-source, local-first voice-to-text dictation application built to give users a fast, private, and subscription-free alternative to commercial dictation software. Contributions of all kinds—code, documentation, bug reports, feature suggestions, UI improvements, and language models—are welcome and celebrated!

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Improving Documentation](#improving-documentation)
  - [Code Contributions](#code-contributions)
- [Development Setup](#development-setup)
- [Project Architecture](#project-architecture)
- [Coding Guidelines](#coding-guidelines)
- [Commit & Pull Request Guidelines](#commit--pull-request-guidelines)
- [Questions and Support](#questions-and-support)

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please report any unacceptable behavior to the project maintainers.

---

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check existing [GitHub Issues](https://github.com/Jatin-nicon/DhwaniLekh/issues) to ensure it hasn't already been reported.

If it's new, please open an issue using the **Bug Report** template and include:
- A clear description of the issue.
- Step-by-step instructions to reproduce.
- Your OS, Python version, Whisper model size, and audio hardware setup.
- Relevant terminal logs or error tracebacks.

### Suggesting Features

We actively encourage ideas for new capabilities! Please open an issue using the **Feature Request** template. Some great areas to explore:
- **System Tray & Floating UI Overlay**: Minimalist status indicator showing when recording / transcribing.
- **Cross-Platform Support**: Extending keyboard hooks and clipboard injection to Linux (Wayland/X11) and macOS.
- **Multilingual Punctuation & Formatting**: Expanding spoken formatting commands for Hindi, Spanish, German, French, etc.
- **Local LLM Post-Processing**: Optional local LLM rewrites (e.g., using Ollama or llama.cpp for concise/email formatting).
- **Streaming Transcription**: Real-time live preview while speaking.

### Improving Documentation

Documentation improvements (clarifying setup steps, adding diagrams, fixing typos, writing guides) are always appreciated!

---

## Development Setup

### 1. Prerequisites

- **Python 3.9+** (Python 3.10, 3.11, or 3.12 recommended)
- **Git**
- Working microphone connected to your machine

### 2. Fork and Clone

```bash
git clone https://github.com/<your-username>/DhwaniLekh.git
cd DhwaniLekh
```

### 3. Create a Virtual Environment

**On Windows (PowerShell / Command Prompt):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**On Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

Install the project in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

Or using `requirements-dev.txt`:

```bash
pip install -r requirements-dev.txt
```

### 5. Run the Application Locally

```bash
python run.py
```

Or using the installed package entrypoint:

```bash
dhwanilekh
```

### 6. Run the Test Suite

Run unit tests with pytest:

```bash
pytest -v
```

Or via Python's built-in unittest runner:

```bash
python -m unittest discover -s tests
```

---

## Project Architecture

The codebase is organized in a modular structure under `src/dhwanilekh`:

```
DhwaniLekh/
├── .github/                 # Issue/PR templates and CI workflow
├── docs/                    # Architecture, Roadmap, Comparison docs
├── src/
│   └── dhwanilekh/
│       ├── __init__.py      # Package metadata & version
│       ├── __main__.py      # Enables `python -m dhwanilekh`
│       ├── app.py           # Application coordinator & event loop
│       ├── audio.py         # Microphone capture & stream recorder
│       ├── cleaner.py       # Spoken punctuation & text formatting
│       ├── config.py        # Settings management & JSON persistence
│       ├── feedback.py      # Audio / TTS user feedback
│       ├── injector.py      # Clipboard & keystroke injection
│       └── transcriber.py   # faster-whisper model manager & inference
├── tests/                   # Unit and integration test suite
├── pyproject.toml           # Modern package configuration
├── requirements.txt         # Core dependencies
├── requirements-dev.txt     # Development & testing dependencies
├── run.py                   # Root execution script
└── start_dhwanilekh.bat     # Windows launcher script
```

For a comprehensive explanation of component interactions, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## Coding Guidelines

- **PEP 8**: Follow standard Python style guidelines.
- **Type Hints**: Include type hints (`typing`) on function signatures and class methods.
- **Docstrings**: Document classes, methods, and non-trivial functions using Google or standard Python docstring format.
- **Decoupled Design**: Keep audio capture, transcription, text post-processing, and window injection decoupled to ensure each module remains easily testable in isolation.
- **Privacy & Security**: DhwaniLekh is strictly local-first. Never introduce features that transmit user audio, keystrokes, or transcriptions over the internet without explicit, opt-in consent.

---

## Commit & Pull Request Guidelines

### Conventional Commits

We recommend following conventional commit messages:

- `feat: add floating recording overlay`
- `fix: resolve clipboard race condition in text injector`
- `docs: update setup guide for CUDA acceleration`
- `test: add unit tests for spoken comma formatting`
- `refactor: extract audio streamer into dedicated worker`

### Submitting a Pull Request

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```
2. Make your changes with focused, descriptive commits.
3. Verify all tests pass:
   ```bash
   pytest
   ```
4. Push your branch to your fork:
   ```bash
   git push origin feat/your-feature-name
   ```
5. Open a Pull Request against the `main` branch of `Jatin-nicon/DhwaniLekh`.
6. Fill in the Pull Request template details. Maintainers will review and provide constructive feedback!

---

## Questions and Support

Feel free to open an issue or start a Discussion on GitHub. Thank you for helping build DhwaniLekh!

