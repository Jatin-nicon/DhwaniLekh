@echo off
title DhwaniLekh - Local Voice Dictation
cd /d "%~dp0"

if exist "project\wispr_free\.venv\Scripts\activate.bat" (
    call "project\wispr_free\.venv\Scripts\activate.bat"
) else if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
)

python run.py
pause
