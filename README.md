<div align="center">

# 🎙️ DhwaniLekh (ध्वनिलेख)

### *Fast, Local-First, Privacy-Focused Voice-to-Text Dictation for Your Desktop*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Status: MVP](https://img.shields.io/badge/status-active%20development-orange.svg)](docs/ROADMAP.md)

[Features](#-features) •
[Quickstart](#-quickstart) •
[Usage](#-usage) •
[Configuration](#-configuration) •
[Architecture](#-architecture) •
[Roadmap](#-roadmap) •
[Contributing](#-contributing)

</div>

---

## 💡 What is DhwaniLekh?

**DhwaniLekh** (*Dhwani* = Voice / Sound, *Lekh* = Writing / Script) is a free, open-source, system-wide desktop dictation tool inspired by apps like Wispr Flow and Superwhisper. 

Instead of routing your personal voice data to expensive cloud APIs or locking you into monthly subscriptions, DhwaniLekh runs **100% locally on your computer** using state-of-the-art quantized Whisper neural models via `faster-whisper`.

Press a global hotkey from inside **any application**—Slack, Word, Visual Studio Code, Chrome, Notion, or your terminal—speak naturally, and watch your words appear in your active text box.

---

## ✨ Features

- 🔒 **100% Local & Private**: No audio or text ever leaves your machine. Full offline capabilities with zero telemetry.
- ⚡ **Lightning-Fast Inference**: Uses `faster-whisper` (CTranslate2) with `int8` quantization for smooth, low-latency CPU transcription.
- ⌨️ **System-Wide Universal Paste**: Works in any app or text field via clipboard paste or simulated keystrokes.
- 🗣️ **Spoken Punctuation**: Automatically converts spoken commands like *"comma"*, *"period"*, *"question mark"*, and *"new line"* into standard punctuation.
- 🔄 **Smart Capitalization & Normalization**: Capitalizes start of sentences, trims redundant spaces, and formats text cleanly.
- 🔊 **Voice & Audio Feedback**: Optional spoken audio notifications let you know when recording starts, transcribes, and completes.
- 🎛️ **Extensible & Configurable**: Easily tweak hotkeys, Whisper model sizes (`tiny`, `base`, `small`, `medium`), language, and typing modes.
- 💸 **Forever Free & Open Source**: Licensed under MIT. No credits, no subscriptions, no rate limits.

---

## 🚀 Quickstart

### Prerequisites

- **Python 3.9+** (Python 3.10, 3.11, or 3.12 recommended)
- **Git**
- A working microphone

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jatin-nicon/DhwaniLekh.git
   cd DhwaniLekh
   ```

2. **Set up a virtual environment:**
   ```bash
   # On Windows
   python -m venv .venv
   .\.venv\Scripts\activate

   # On Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -e .
   ```

4. **Launch DhwaniLekh:**
   ```bash
   python run.py
   ```
   *(On Windows, you can also double-click `start_dhwanilekh.bat`)*

> **Note**: On the very first run, DhwaniLekh will automatically download the lightweight Whisper model (approx. 140MB for the `base` model). Subsequent starts will load immediately from your local cache.

---

## 🎯 Usage

1. **Start DhwaniLekh**: Run `python run.py`. You'll hear *"DhwaniLekh is ready"* (if speech feedback is enabled).
2. **Focus any window**: Click into any text field or application (e.g., Notepad, VS Code, Slack, WhatsApp, Browser).
3. **Trigger recording**: Press <kbd>Ctrl</kbd> + <kbd>Space</kbd> (configurable).
4. **Speak**: Talk naturally. You can speak punctuation:
   - *"Hello comma how are you question mark"* ➔ `Hello, how are you?`
   - *"Please see the following new line item one period"* ➔ `Please see the following` <br> `Item one.`
5. **Paste**: Press <kbd>Ctrl</kbd> + <kbd>Space</kbd> again. DhwaniLekh stops recording, transcribes your speech, formats it, and types it directly into your active cursor position.

---

## ⚙️ Configuration

DhwaniLekh stores its configuration in `settings.json` in the root directory. It is automatically created on first launch if it does not exist:

```json
{
  "hotkey": "ctrl+space",
  "model_size": "base",
  "compute_type": "int8",
  "sample_rate": 16000,
  "language": "en",
  "paste_mode": "clipboard",
  "speak_status": true
}
```

### Configuration Options

| Option | Type | Default | Description |
|---|---|---|---|
| `hotkey` | string | `"ctrl+space"` | Global hotkey combo to toggle dictation (e.g., `"ctrl+alt+d"`, `"f8"`). |
| `model_size` | string | `"base"` | Whisper model size: `"tiny"`, `"base"`, `"small"`, `"medium"`, or `"large-v3"`. |
| `compute_type` | string | `"int8"` | Inference precision: `"int8"` (fastest on CPU), `"float16"` (recommended for GPU), or `"float32"`. |
| `sample_rate` | integer | `16000` | Audio sampling frequency (Whisper natively operates at 16,000 Hz). |
| `language` | string / null | `"en"` | Language code (e.g., `"en"`, `"hi"`, `"es"`, `"fr"`). Set to `null` for automatic language detection. |
| `paste_mode` | string | `"clipboard"` | `"clipboard"` (fast paste via simulated Ctrl+V) or `"typing"` (character-by-character typing). |
| `speak_status` | boolean | `true` | Whether to announce recording status via text-to-speech. |

---

## 🧠 Architecture

```
User Hotkey (Ctrl+Space)
          │
          ▼
┌──────────────────┐
│  AudioRecorder   │ ──► Streams microphone audio via sounddevice (16kHz)
└──────────────────┘
          │
          ▼
┌──────────────────┐
│   Transcriber    │ ──► On-device STT with faster-whisper (VAD enabled)
└──────────────────┘
          │
          ▼
┌──────────────────┐
│   TextCleaner    │ ──► Replaces spoken punctuation & normalizes casing
└──────────────────┘
          │
          ▼
┌──────────────────┐
│   TextInjector   │ ──► Copies to clipboard & triggers Ctrl+V in active app
└──────────────────┘
```

For an in-depth breakdown of module interactions and threading design, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## 📂 Project Structure

```
DhwaniLekh/
├── .github/
│   ├── ISSUE_TEMPLATE/       # Bug report & feature request templates
│   ├── workflows/            # GitHub Actions CI workflow
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── ARCHITECTURE.md       # Technical design and pipeline details
│   ├── COMPARISON.md         # DhwaniLekh vs Wispr Flow & alternatives
│   └── ROADMAP.md            # Upcoming milestones and features
├── src/
│   └── dhwanilekh/
│       ├── __init__.py       # Package definition
│       ├── __main__.py       # Module entrypoint (`python -m dhwanilekh`)
│       ├── app.py            # Main application coordinator
│       ├── audio.py          # Sounddevice microphone recorder
│       ├── cleaner.py        # Text post-processing & spoken punctuation
│       ├── config.py         # Settings & configuration loader
│       ├── feedback.py       # Audio & TTS status announcements
│       ├── injector.py       # Cross-app clipboard & typing injection
│       └── transcriber.py    # faster-whisper inference wrapper
├── tests/
│   ├── test_cleaner.py       # Unit tests for text normalization
│   └── test_config.py        # Unit tests for settings management
├── .gitignore
├── CHANGELOG.md              # Version release history
├── CODE_OF_CONDUCT.md        # Contributor Covenant v2.1
├── CONTRIBUTING.md           # How to setup dev environment & contribute
├── LICENSE                   # MIT License
├── pyproject.toml            # Modern PEP 517/621 packaging metadata
├── README.md                 # Project front page
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development & testing dependencies
├── run.py                    # Root entrypoint
└── start_dhwanilekh.bat      # Quick-launch script for Windows
```

---

## 🗺️ Roadmap

Check out our [Project Roadmap](docs/ROADMAP.md) to see what is planned next! Key upcoming highlights:

- [ ] **Desktop System Tray & Floating Overlay**: Visual pill indicating when listening/transcribing.
- [ ] **Cross-Platform Support**: Linux (Wayland/X11) and macOS compatibility.
- [ ] **Local LLM Rewriting**: Optional integration with local models (via Ollama or llama.cpp) for smart punctuation, concise summaries, and email drafts.
- [ ] **Custom Vocabulary**: User-defined dictionary for domain-specific acronyms and phrases.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**!

Please read our [Contributing Guide](CONTRIBUTING.md) to get started with local development, running tests, and submitting pull requests.

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more details.

---

<div align="center">
Built with ❤️ for privacy, accessibility, and open-source freedom.
</div>
