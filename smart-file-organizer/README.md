# 🗂️ Professional File Organizer

A powerful and user-friendly Python tool to automatically organize your messy files into categorized folders based on file type and date.

## ✨ Features

- **Smart Categorization**: Automatically sorts files into 8 predefined categories
  - 📷 Images (jpg, png, gif, etc.)
  - 🎥 Videos (mp4, avi, mkv, etc.)
  - 📄 Documents (pdf, docx, xlsx, etc.)
  - 🎵 Audio (mp3, wav, flac, etc.)
  - 📦 Archives (zip, rar, 7z, etc.)
  - 💻 Programming (py, js, html, etc.)
  - 📱 Applications (exe, apk, dmg, etc.)
  - 📂 Others (uncategorized files)

- **Flexible Organization Options**:
  - Organize by file type only
  - Organize by date only (year/month)
  - Organize by both type and date (recommended)

- **Safe File Handling**:
  - Automatic duplicate file renaming
  - Preserves original files
  - Detailed error reporting
  - Skips hidden files automatically

- **Detailed Statistics**:
  - Total files processed
  - Successfully organized files
  - Skipped files count
  - Error tracking
  - Success rate percentage

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/Airfidu/file-organizer.git
cd file-organizer
```

2. Install requirements (optional, no external packages needed):
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

Run the script:
```bash
python file_organizer.py
```

### Interactive Mode

The script will prompt you for:

1. **Folder path**: Enter the path to organize, or press Enter for current directory
2. **Organization method**: Choose from three options:
   - `1` - Organize by type only
   - `2` - Organize by date only
   - `3` - Organize by type and date (recommended)
3. **Confirmation**: Confirm to proceed with organization

### Example

```
🗂️  Professional File Organizer
============================================================

📂 Enter the folder path to organize:
   (or press Enter to use current folder)
Path: /Users/username/Downloads

⚙️  Organization options:
1. Organize by type only
2. Organize by date only
3. Organize by type and date (recommended)

Choose method (1-3) [default: 3]: 3

⚠️  Files will be organized in: /Users/username/Downloads
Do you want to continue? (yes/no) [yes]: yes

🚀 Starting file organization in: /Users/username/Downloads
============================================================
✅ Moved: photo.jpg
   → To: Images/2025/01-January/photo.jpg
✅ Moved: document.pdf
   → To: Documents/2025/01-January/document.pdf
...
```

## 📁 Folder Structure Examples

### By Type and Date (Recommended)
```
Downloads/
├── Images/
│   ├── 2025/
│   │   ├── 01-January/
│   │   └── 02-February/
│   └── 2024/
├── Documents/
│   ├── 2025/
│   └── 2024/
└── Videos/
    └── 2025/
```

### By Type Only
```
Downloads/
├── Images/
├── Documents/
├── Videos/
└── Audio/
```

### By Date Only
```
Downloads/
├── 2025/
│   ├── 01-January/
│   └── 02-February/
└── 2024/
    └── 12-December/
```

## 🛡️ Safety Features

- **No Data Loss**: Files are moved, not copied or deleted
- **Duplicate Handling**: Automatically renames duplicates with `_1`, `_2`, etc.
- **Hidden Files**: Skips hidden files (starting with `.`)
- **Error Recovery**: Continues processing even if individual files fail
- **Detailed Logging**: Shows exactly what happened to each file

## 📊 Statistics Output

After organizing, you'll see detailed statistics:

```
============================================================
📊 Organization Statistics:
============================================================
📁 Total files: 150
✅ Organized files: 145
⏭️  Skipped files: 3
❌ Errors: 2
============================================================
🎯 Success rate: 96.7%

✨ Organization completed successfully!
```

## ⚙️ Customization

You can easily customize file categories by editing the `categories` dictionary in the `FileOrganizer` class:

```python
self.categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'YourCategory': ['.ext1', '.ext2'],
    # Add more categories...
}
```

## 🙏 Acknowledgments

- Built with Python's standard library
- Inspired by the need for clean and organized file systems
- Thanks to all contributors!

---

**Made with ❤️ by [Airfidu]**
