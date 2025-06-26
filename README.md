# Custom File System

A custom in-memory, block-based file system simulator written in Python. This project demonstrates how files and directories are stored, organized, and accessed on a disk, covering core concepts including file operations, directory structure, metadata management, and block allocation.

---

## 🚀 Project Overview

This prototype implements:

- **File Operations**
  - Create files with content
  - Read file contents
  - Delete files
  - File metadata tracking (size, creation time, modification time)
- **Directory Structure**
  - Hierarchical directory organization
  - Support for absolute and relative paths
  - Directory navigation commands (`cd`, `mkdir`, `ls`, `pwd`)
- **Block Management**
  - Bitmap-based block allocation
  - Support for files spanning multiple 512-byte blocks
  - Efficient space management and deallocation
- **Persistence**
  - File system state saved between sessions
  - Metadata stored in `fs_metadata.pkl`
  - Virtual disk image in `disk.img` persists data

---

## 🧩 Repository Structure

```
CustomFileSystem/
├── main.py          # Entry point: initializes Disk, FileSystem, and starts the shell
├── disk.py          # Virtual disk implementation (read/write 512 B blocks)
├── filesystem.py    # Core FS functionality: file/dir ops, metadata, persistence
├── directory.py     # Directory tree implementation and path resolution
├── bitmap.py        # Block allocation management via a bitmap
├── shell.py         # Interactive command-line interface
├── disk.img         # Virtual disk image file (auto-generated)
├── fs_metadata.pkl  # Persisted file system metadata (auto-generated)
├── PROTOTYPE.md     # Quickstart guide and design notes
├── Write-Up.docx    # Detailed explanation of design choices and data structures
└── README.md        # This file
```

---

## 🔧 Prerequisites

- **Python 3.7+**  
- No external dependencies beyond the Python standard library.

---

## 🛠️ Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/CustomFileSystem.git
   cd CustomFileSystem
   ```

2. **Run the file system**  
   ```bash
   python main.py
   ```
   This creates `disk.img` and `fs_metadata.pkl` on first run and starts the shell prompt:
   ```
   /> 
   ```

---

## 📚 Shell Commands

| Command             | Description                                             |
|---------------------|---------------------------------------------------------|
| `help`              | Show available commands.                                |
| `mkdir <dirname>`   | Create a new directory in the current directory.        |
| `cd <path>`         | Change directory (absolute or relative paths).          |
| `ls [path]`         | List contents of current or specified directory.        |
| `pwd`               | Print the current working directory path.               |
| `create <filename>` | Create a new file; prompts for content input.           |
| `read <filename>`   | Display the contents of a file.                         |
| `delete <name>`     | Delete a file or empty directory.                       |
| `clear`             | Clear the terminal screen.                              |
| `exit`              | Persist state and exit the shell.                       |

---

## 🔍 Technical Details

### File System Design

- **Block Size**: 512 bytes  
- **Disk Size**: 1 MB (2048 blocks)  
- **Block Allocation**: Bitmap-based tracking of free/used blocks  
- **Directory Structure**: Tree-based with parent-child relationships  
- **Metadata Storage**: Pickled directory tree and free-block bitmap in `fs_metadata.pkl`

### Components

1. **Disk Layer (`disk.py`)**  
   - Manages `disk.img` file  
   - Provides `read_block(block_num)` and `write_block(block_num, data)`  

2. **Bitmap (`bitmap.py`)**  
   - Tracks block allocation via a list of bits  
   - `allocate_block()` and `deallocate_block(block_num)` operations  

3. **Directory (`directory.py`)**  
   - Represents directories with `name`, `parent`, and `entries`  
   - Resolves absolute and relative paths without circular references  

4. **FileSystem Core (`filesystem.py`)**  
   - Implements `create_file`, `read_file`, `delete_file`, `mkdir`, `ls`, `cd`  
   - Manages metadata and persistence (`save_metadata`, `load_metadata`)  

5. **Shell Interface (`shell.py`)**  
   - Provides an interactive prompt  
   - Parses and dispatches commands to `FileSystem` methods  

---

## 🎯 Deliverables & Milestones

1. **Write-up Documentation (`Write-Up.docx`)**  
   - Detailed explanation of data structures and algorithms  
   - Comparisons with real-world file systems  
   - Design rationale and improvement suggestions  

2. **Prototype Implementation**  
   - Core source code modules (`*.py`)  
   - Quickstart guide (`PROTOTYPE.md`)  
   - Virtual disk (`disk.img`) and metadata (`fs_metadata.pkl`)  

3. **Final Presentation**  
   - Summary of design and functionality  
   - Live demonstration of shell commands  
   - Architecture overview and Q&A  

---

## 🚀 Next Steps

- **Permissions & ACLs**: Add user/group access controls  
- **Journaling**: Implement crash-safe metadata journaling  
- **Performance**: Optimize block search with free-block queues  
- **Advanced Metadata**: Support extended attributes and links  

---

## 📬 Contact & Contributions

Contributions and feedback are welcome!  
Open an issue or submit a pull request, or contact **kothakonda.baby@gmail.com**.
