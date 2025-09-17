# Text File Splitter

A Windows Forms application for splitting large text files into smaller chunks, specifically designed for Cold Turkey Blocker import compatibility.

Built with .NET 9.0 Windows Forms.

## Features

- Split large text files into smaller chunks of a specified size
- Automatically filters out empty lines and comments (lines starting with #)
- Creates output files in a `hosts_chunks` subdirectory
- Progress bar and status updates during processing
- Administrator privileges enforcement via manifest

## Requirements

- Windows OS
- .NET 9.0 Runtime or higher

## Usage

1. Run the application using the `run.bat` file (administrator privileges will be requested automatically)
2. Click "Browse..." to select the input text file to split
3. Enter the desired chunk size (default is 4900 lines for Cold Turkey Blocker compatibility)
4. Optionally specify an output directory (if not specified, chunks will be created in the same directory as the input file)
5. Click "Split File" to begin processing

The application will create a `hosts_chunks` folder in the output directory and split the input file into multiple parts with names like:
- `hosts_part_01_of_16.txt`
- `hosts_part_02_of_16.txt`
- etc.

## Building from Source

To build the application from source:

1. Open a command prompt in the project directory
2. Run `dotnet build -c Release`
3. The executable will be created in the `bin\Release\net9.0-windows` folder

## Downloading the Executable

You can download the latest compiled version of the application from the [Releases](https://github.com/mackka2k/Text-File-Splitter/releases) page.

## Testing

To test the application:

1. Run `test_app.ps1` to create a test input file and launch the application
2. In the application:
   - Select `test_input.txt` as the input file
   - Set chunk size to 3
   - Click "Split File"
3. Check the `hosts_chunks` directory for the output files

## License

This project is provided for educational and research purposes only. Please ensure you comply with all applicable laws and the terms of service of any software you are researching.