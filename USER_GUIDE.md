# Text File Splitter - User Guide

## Overview

Text File Splitter is a Windows application that helps you split large text files into smaller chunks. It's particularly useful for Cold Turkey Blocker users who need to import large domain lists that exceed the application's import limits.

## Getting Started

### Prerequisites

- Windows operating system
- .NET 9.0 Runtime installed

### Running the Application

1. Double-click the `run.bat` file to launch the application
2. If prompted, allow the application to run with administrator privileges

## Using the Application

### 1. Select Input File

- Click the "Browse..." button next to "Input Text File"
- Navigate to and select the text file you want to split
- The file should contain one entry per line (e.g., domain names)

### 2. Set Chunk Size

- Enter the maximum number of lines per chunk in the "Chunk Size" field
- For Cold Turkey Blocker, the recommended size is 4900 (which is the default)
- You can adjust this based on your needs

### 3. Select Output Directory (Optional)

- By default, output files will be created in the same directory as the input file
- To specify a different output location, click the "Browse..." button next to "Output Folder"

### 4. Split the File

- Click the "Split File" button to begin processing
- The progress bar will show the status of the operation
- Status messages will appear below the progress bar

### 5. Check Results

- After processing completes, a message box will confirm success
- The application creates a `hosts_chunks` subdirectory in your output location
- Inside this directory, you'll find the split files named:
  - `hosts_part_01_of_XX.txt`
  - `hosts_part_02_of_XX.txt`
  - etc.

## Features

### Automatic Filtering

The application automatically filters out:
- Empty lines
- Lines containing only whitespace
- Comments (lines starting with #)

### Progress Tracking

- Progress bar shows overall completion status
- Status messages provide detailed information about the current operation
- File creation notifications show the name and line count of each chunk

### Administrator Privileges

The application requests administrator privileges to ensure it can:
- Access protected directories
- Create files in system locations if needed
- Handle large file operations without permission issues

## Troubleshooting

### "File not found" Error

- Ensure the input file path is correct
- Verify the file exists and is accessible
- Check that you have read permissions for the file

### "Access denied" Error

- Make sure the application is running with administrator privileges
- Verify you have write permissions for the output directory
- Try selecting a different output location (e.g., your Documents folder)

### Application Freezes During Processing

- Large files may take some time to process
- Do not close the application while the progress bar is active
- Check the status messages for progress updates

## Technical Details

### File Format

The application expects text files with one entry per line. It works well with:
- Hosts files
- Domain lists
- Word lists
- Any line-based text format

### Output Format

- Each output file contains up to the specified number of lines
- Empty lines and comments are excluded from the count
- Files are named sequentially with zero-padded numbers
- Output files are created in UTF-8 encoding

### Performance

- The application processes files asynchronously to keep the UI responsive
- Large files are handled efficiently using streaming techniques
- Memory usage is optimized for handling very large input files

## Support

For issues with the application, please check:
1. That you're using the latest version
2. That all prerequisites are installed
3. The troubleshooting section above

This is an educational tool provided for research purposes. Please ensure you comply with all applicable laws and software licenses.