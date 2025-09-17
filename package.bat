@echo off
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File package_app.ps1
pause