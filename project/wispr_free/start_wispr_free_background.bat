@echo off
cd /d "%~dp0"
set "PYW=%~dp0.venv\Scripts\pythonw.exe"
set "PY=%~dp0.venv\Scripts\python.exe"
set "APP=%~dp0app.py"

if exist "%PYW%" (
    start "WisprFree" /min "%PYW%" "%APP%"
) else if exist "%PY%" (
    start "WisprFree" /min "%PY%" "%APP%"
) else (
    echo Could not find Python in .venv\Scripts
    pause
)
exit
