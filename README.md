
```markdown
# Document Organizer

A Python script that searches for document files across different storage locations and organizes them by file type in a specified directory.

## Features

- Recursively searches for files in:
  - All available drives (Windows)
  - Root directory (Linux)
  - Termux shared storage (Android)
- Organizes files by extension into categorized folders
- Generates a log file with copy operations and statistics
- Handles common file types: DOC, DOCX, TXT, RTF, ODT, PDF, XLS, XLSX, PPT, PPTX

## Requirements

- Python 3.x
- Termux environment (for Android functionality)
- Appropriate file permissions

## Usage

1. Run the script:
   ```bash
   python project.py
   ```
2. When prompted, enter the path where you want to save the organized documents
   Example:
   ```
   Enter the path to save data: /storage/emulated/0/Documents
   ```

The script will:
- Create a "documents" directory at your specified path
- Create subdirectories for each file type
- Copy all found documents to their respective folders
- Generate an "info.txt" log file with operation details

## File Structure

After execution, your target directory will contain:
```
documents/
├── DOC/
├── DOCX/
├── TXT/
├── RTF/
├── ODT/
├── PDF/
├── XLS/
├── XLSX/
├── PPT/
├── PPTX/
└── info.txt
```

## Notes

- The script handles permission errors gracefully
- Will not overwrite existing files (SameFileError protection)
- Includes timing metrics for performance monitoring
- Log file contains:
  - Source and destination paths for copied files
  - Total files searched
  - Total files copied
  - Execution time

## Warning

This script will access filesystem-wide locations. Ensure you:
- Have proper permissions
- Understand it will copy (not move) files
- Review the info.txt log after execution
```

This README provides:
1. Clear purpose description
2. Usage instructions
3. Expected output structure
4. Important notes about functionality
5. Appropriate warnings

You may want to adjust the "Requirements" section based on any specific dependencies your script needs, or add installation instructions if this becomes part of a larger package.