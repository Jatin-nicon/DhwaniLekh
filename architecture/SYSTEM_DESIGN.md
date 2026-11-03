# System Design

## Core pipeline
1. Hotkey pressed
2. Record microphone input
3. Save temporary audio buffer
4. Run transcription engine
5. Clean / post-process text
6. Insert text into active application
7. Optionally run rewrite mode

## Candidate stack
- Python
- faster-whisper or whisper.cpp
- sounddevice
- keyboard
- pyperclip
- pyautogui
- optional AutoHotkey integration

## Core modules
- `audio_capture`
- `transcription`
- `text_cleanup`
- `text_insertion`
- `hotkey_listener`
- `settings`
- `rewrite_modes`

## Hard parts
- low latency
- reliable insertion across apps
- noisy microphone environments
- natural punctuation and cleanup
- good UX
