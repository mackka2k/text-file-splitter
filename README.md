# Text File Splitter

Splits files. Filters comments (`#`) and empty lines automatically because nobody wants junk in their chunks.

## How to use (for people who read docs)

### Use the EXE (Recommended)
1. Go to `dist/`.
2. Run `TextFileSplitter.exe`. No, you don't need to install anything.

### Build it yourself (if you must)
1. Install dependencies: `pip install customtkinter Pillow pyinstaller`
2. Run `build.bat`.
3. Wait for PyInstaller to do its thing.

### Clean up the mess
- Run `clean.bat`. It nukes `build/`, `dist/`, and other junk.

### Run from source (dev mode)
- `python main.py`

## Logic
- **Input**: UTF-8 text.
- **Output**: UTF-8 chunks in `hosts_chunks/`.
- **Filtering**: Lines starting with `#` are ignored. Whitespace is stripped.

## Stats
- GUI: `customtkinter` (retro style, obviously).
- Logic: `python` (simplicity over C# bloat).
- Window: 650x520 (Fixed size. Don't try to stretch it).

---
*Legacy code removed. Move fast, break things, then fix them in Python.*