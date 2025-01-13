# python-tools
Used for integrating some small tools written in Python
# DOC to Markdown Converter

This Python script converts DOC files to Markdown format using LibreOffice and Pandoc.

## Requirements

- Python 3.x
- LibreOffice (for DOC to DOCX conversion)
- Pandoc (for DOCX to Markdown conversion)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/)
2. Install LibreOffice:
   - Ubuntu/Debian: `sudo apt install libreoffice`
   - macOS: `brew install libreoffice`
   - Windows: Download from [libreoffice.org](https://www.libreoffice.org/)
3. Install Pandoc:
   - Ubuntu/Debian: `sudo apt install pandoc`
   - macOS: `brew install pandoc`
   - Windows: Download from [pandoc.org](https://pandoc.org/installing.html)

## Usage

1. Place your DOC file in the same directory as the script
2. Run the script:
   ```bash
   python convert_doc_to_md.py
   ```
3. The script will:
   - Convert the DOC file to DOCX using LibreOffice
   - Convert the DOCX file to Markdown using Pandoc
   - Save the output as a .md file with the same base name
   - Clean up temporary files

## Example

Given a file `example.doc`, running the script will produce `example.md`.

## Notes

- The script currently processes `example.doc` by default
- To process other files, modify the `input_file` variable in the script
- Temporary DOCX files are automatically deleted after conversion
- Conversion errors will be printed to the console

## License

This project is open source and available under the MIT License.
