@echo off
title DhwaniLekh - Local Voice Dictation
cd /d "%~dp0"

if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
)

python run.py
pause
