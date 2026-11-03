# DhwaniLekh Project Roadmap

Welcome to the development roadmap for **DhwaniLekh**. If you're looking to contribute, this roadmap highlights current milestones, near-term priorities, and long-term goals.

---

## Current Status: Phase 1 — MVP (Completed :white_check_mark:)

- [x] Global hotkey toggle (`Ctrl+Space`) to start and stop speech capture.
- [x] Local offline microphone capture via `sounddevice`.
- [x] On-device transcription using `faster-whisper`.
- [x] Spoken punctuation substitution ("comma", "period", "new line").
- [x] Universal paste injection into the active desktop application.
- [x] Spoken voice feedback via TTS (`pyttsx3`).
- [x] Modular codebase architecture and automated unit test suite.

---

## Phase 2: Enhanced Text Formatting & Usability (In Progress :hammer:)

Focus: Improving everyday dictation quality and giving users better controls.

- [ ] **Rich Spoken Punctuation**: Expand spoken tokens (e.g., quotes, bullet points, numbered lists, brackets).
- [ ] **Multilingual Punctuation**: Add language-specific cleanup dictionaries (e.g. Hindi, Spanish, French, German).
- [ ] **Sound Effects**: Add optional lightweight chime sounds (start/stop audio cues) as a snappier alternative to TTS.
- [ ] **Custom Dictionary / Replacement Rules**: Allow users to define custom word replacements and vocabulary lists in `settings.json`.
- [ ] **Clipboard History Preservation**: Option to restore previous clipboard contents after pasting dictation.

---

## Phase 3: Desktop UI & Visual Feedback

Focus: Providing visual indicators so users know when DhwaniLekh is recording or processing.

- [ ] **System Tray Icon**: Windows notification area tray icon with status menu, settings shortcut, and exit option.
- [ ] **Floating Overlay / Pill**: Minimalist, unobtrusive floating indicator or microphone pill that animates while recording.
- [ ] **Interactive Settings GUI**: Simple window to configure hotkeys, Whisper models, audio devices, and languages without editing JSON directly.

---

## Phase 4: Local AI Rewrite & Modes

Focus: Intelligent text formatting powered by lightweight local LLMs (e.g., via Ollama, llama.cpp).

- [ ] **Rewrite Modes**:
  - `Clean`: Removes filler words ("um", "uh", "like") and tightens phrasing.
  - `Concise`: Summarizes thoughts into brief bullet points.
  - `Professional`: Polishes grammar and tone for professional email correspondence.
- [ ] **Voice Commands**: Voice-triggered actions (e.g., "delete last sentence", "send message").

---

## Phase 5: Cross-Platform Support

Focus: Bringing DhwaniLekh to developers and users on Linux and macOS.

- [ ] **Linux Support**: Implement Wayland & X11 input hooks and clipboard tools (`wl-clipboard`, `xclip`).
- [ ] **macOS Support**: Implement macOS accessibility permissions and AppleScript key emulation.

---

## How to Pick Up an Item

If you want to contribute to an item on this roadmap:
1. Check the [GitHub Issues](https://github.com/Jatin-nicon/DhwaniLekh/issues) to see if someone is already working on it.
2. If not, open a new Issue referencing the roadmap item (e.g., *"Phase 2: Add customizable dictionary support"*).
3. Follow the instructions in [CONTRIBUTING.md](../CONTRIBUTING.md) to submit your PR.
