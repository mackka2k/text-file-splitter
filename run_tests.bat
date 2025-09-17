@echo off
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File test_app.ps1
pause