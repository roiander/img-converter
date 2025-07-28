# Free Image Converter

A simple, user-friendly Python application that allows you to convert multiple images to various formats (like WebP, PNG, JPEG) and package them into a ZIP or RAR archive. Supports drag-and-drop functionality for easy use!

## Features
- **Drag and Drop**: Easily add images by dragging them from your file explorer.
- **Multiple Formats**: Convert to WebP, PNG, JPEG, JPG, BMP, or GIF.
- **Archive Options**: Package converted images into ZIP or RAR files.
- **Temporary Processing**: Handles conversions in a temp directory to keep your system clean.
- **Cross-Platform**: Built with Tkinter, works on Windows (and potentially others with adjustments).

## Prerequisites
- Python 3.x installed.
- For RAR archiving: Ensure you have the `rar` command-line tool installed and available in your system's PATH.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/free-image-converter.git
   cd free-image-converter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include:
   - Pillow (for image processing)
   - tkinterdnd2 (for drag-and-drop support)
   - patool (for archiving)

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. **Drag and Drop Images**: Drag images from your file explorer into the gray area of the app window.

3. **Select Output Format**: Choose from the dropdown (e.g., webp, png, jpeg).

4. **Select Archive Type**: Choose ZIP or RAR.

5. **Convert and Package**: Click the "Convert and Package" button. You'll be prompted to save the archive file.

6. A success message will appear, and your archive will be ready without unnecessary folder structures!

## Screenshots

*(Add screenshots here for a visual guide, e.g., app interface, drag-drop action)*

## Troubleshooting
- **ModuleNotFoundError**: Ensure all dependencies are installed correctly. Run `pip install -r requirements.txt` again.
- **RAR Issues**: If RAR creation fails, verify `rar.exe` is installed and in PATH.
- **Drag-and-Drop Not Working**: Confirm tkinterdnd2 is properly installed.

## Contributing
Feel free to fork the repo and submit pull requests! If you find bugs or have feature suggestions, open an issue.

## License
This project is open-source and available under the MIT License.

---

Enjoy converting your images effortlessly! 🚀
