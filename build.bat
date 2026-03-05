@echo off
setlocal

:: Get customtkinter path
for /f "delims=" %%i in ('python -c "import customtkinter; import os; print(os.path.dirname(customtkinter.__file__))"') do set CTK_PATH=%%i

if "%CTK_PATH%"=="" (
    echo Error: Could not find customtkinter path.
    exit /b 1
)

echo Building TextFileSplitter...
pyinstaller --noconsole --onefile --name TextFileSplitter --icon app_icon.ico --add-data "%CTK_PATH%;customtkinter/" main.py

if %ERRORLEVEL% == 0 (
    echo Build successful. Executable is in the 'dist' folder.
) else (
    echo Build failed.
)

pause
