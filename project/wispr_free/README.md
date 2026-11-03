# WisprFree

A free local dictation MVP inspired by the Wispr Flow experience.

## What it does
- Runs locally on your computer
- Uses a global hotkey to start/stop recording
- Transcribes speech with `faster-whisper`
- Cleans the text a little
- Pastes into the active app

## How to run
1. Open this folder.
2. Double-click `run_wispr_free.bat`
3. Wait for the app to say or print `Wispr Free is ready.`
4. Press `Ctrl+Space` once to start recording.
5. Speak.
6. Press `Ctrl+Space` again to stop and transcribe.
7. Focus any text box before stopping if you want the text pasted there.

## Notes
- The first run may download the Whisper model automatically.
- Default model is `base` for a balance of speed and quality.
- You can edit `settings.json` to change the hotkey or model size.
- If paste behaves oddly in an app, switch `paste_mode` to `typing`.

## Good next upgrades
- better spoken punctuation commands
- rewrite modes
- tray icon
- transcription history
- wake word mode after hotkey mode is stable
