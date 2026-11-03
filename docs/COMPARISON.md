# DhwaniLekh Comparison & Motivation

This document explains where **DhwaniLekh** fits in the ecosystem of dictation software and why it was built.

---

## Comparison Matrix

| Feature | DhwaniLekh | Wispr Flow | Superwhisper | Windows Voice Typing (`Win + H`) | Raw Whisper Scripts |
|---|:---:|:---:|:---:|:---:|:---:|
| **License & Price** | **100% Free & Open Source (MIT)** | Paid Subscription (~$10–$15/mo) | Paid / Freemium | Free (Requires Windows OS) | Free / Open Source |
| **Data Privacy** | **100% Local / On-Device** | Cloud Processing | Local or Cloud | Cloud Transcribed | Local |
| **Offline Functionality** | :white_check_mark: Full | :x: No (requires internet) | :white_check_mark: Local models | :x: Degrades or fails offline | :white_check_mark: Full |
| **System-wide Paste** | :white_check_mark: Any active field | :white_check_mark: Any active field | :white_check_mark: Any active field | :white_check_mark: Any active field | :x: Usually terminal output only |
| **Global Hotkey** | :white_check_mark: Configurable | :white_check_mark: Fixed/Configurable | :white_check_mark: Configurable | :heavy_minus_sign: Fixed (`Win+H`) | :x: Manual run |
| **Spoken Punctuation** | :white_check_mark: Rule-based & extensible | :white_check_mark: AI formatted | :white_check_mark: AI formatted | :white_check_mark: Basic | :x: None by default |
| **Customizability** | :white_check_mark: Fully open Python stack | :x: Closed source | :x: Closed source | :x: Closed source | :white_check_mark: Open |
| **Multi-Language Support** | :white_check_mark: 99+ Whisper languages | :white_check_mark: Yes | :white_check_mark: Yes | :white_check_mark: Limited to OS packs | :white_check_mark: 99+ languages |

---

## Why DhwaniLekh?

1. **True Privacy**: Sensitive emails, patient notes, proprietary code, and personal thoughts should not be streamed to third-party commercial cloud APIs. DhwaniLekh processes all speech locally on your CPU/GPU.
2. **Zero Subscription Fees**: High-quality voice dictation should be accessible to everyone without recurring monthly payments.
3. **Hackable & Extensible**: Built entirely in Python with clean, modular components. Anyone can plug in custom punctuation rules, connect their favorite local LLM (like Ollama or llama.cpp), or adapt it to their personal workflows.
