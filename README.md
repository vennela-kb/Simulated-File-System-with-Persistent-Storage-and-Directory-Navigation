# Custom File System

A custom file system implementation that simulates how files and directories are stored, organized, and accessed on a disk. This project demonstrates core file system concepts including file operations, directory structure, metadata management, and block allocation.

## Features

- **File Operations**
  - Create files with content
  - Read file contents
  - Delete files
  - File metadata tracking (size, creation time, modification time)

- **Directory Structure**
  - Hierarchical directory organization
  - Support for absolute and relative paths
  - Directory navigation (cd, mkdir, ls, pwd)

- **Block Management**
  - Bitmap-based block allocation
  - Support for files spanning multiple blocks
  - Efficient space management

- **Persistence**
  - File system state is saved between sessions
  - Metadata is stored in a separate file
  - Automatic loading of previous state

## Project Structure

```
CustomFileSystem/
├── main.py          # Entry point and initialization
├── disk.py          # Virtual disk implementation
├── filesystem.py    # Core file system functionality
├── directory.py     # Directory structure implementation
├── bitmap.py        # Block allocation management
├── shell.py         # Command-line interface
├── disk.img         # Virtual disk image
└── fs_metadata.pkl  # File system metadata
```

## Getting Started

1. **Prerequisites**
   - Python 3.x
   - No external dependencies required

2. **Running the File System**
   ```bash
   python main.py
   ```

3. **Available Commands**
   - `mkdir <dirname>`: Create a new directory
   - `cd <dirname>`: Change directory (supports absolute and relative paths)
   - `ls [path]`: List contents of current or specified directory
   - `pwd`: Print current working directory
   - `create <filename>`: Create a new file
   - `read <filename>`: Read file contents
   - `delete <filename>`: Delete a file
   - `clear`: Clear the screen
   - `help`: Show available commands
   - `exit`: Exit the program

## Technical Details

### File System Design

- **Block Size**: 512 bytes
- **Disk Size**: 1MB (configurable)
- **Block Allocation**: Bitmap-based
- **Directory Structure**: Tree-based with parent-child relationships
- **Metadata Storage**: Separate pickle file for persistence

### Key Components

1. **Disk Layer**
   - Simulates physical disk operations
   - Handles block-level read/write operations
   - Manages disk image file

2. **File System Core**
   - Manages file and directory operations
   - Handles block allocation
   - Maintains file system state

3. **Directory Structure**
   - Supports hierarchical organization
   - Implements path resolution
   - Manages file and directory entries

4. **Block Allocation**
   - Uses bitmap for tracking free blocks
   - Supports dynamic block allocation
   - Handles block deallocation

## Deliverables

The project consists of three main deliverables:

1. **Write-up Documentation**
   - Detailed explanation of file system functionality
   - Description of underlying data structures
   - Justification for chosen structures
   - Comparison with other file systems
   - Advantages and improvements over existing systems

2. **Implementation Package**
   - Core file system implementation
   - Disk driver (disk.py)
   - Command-line shell interface
   - Complete source code
   - Documentation on system functionality
   - User guide and setup instructions

3. **Presentation**
   - Summary of write-up content
   - Live demonstration of prototype
   - Technical overview
   - System capabilities showcase
   - Q&A session

### Milestone Deliverables

The project will be developed through several milestones, each with specific deliverables:

1. **Design Phase**
   - File system architecture design
   - Data structure specifications
   - Block allocation strategy
   - Directory structure design
   - Initial documentation

2. **Core Implementation**
   - Basic file operations
   - Directory management
   - Block allocation system
   - Initial shell interface
   - Progress documentation

3. **Advanced Features**
   - Persistence implementation
   - Error handling
   - Advanced file operations
   - Shell improvements
   - Updated documentation

4. **Final Package**
   - Complete implementation
   - Final documentation
   - Presentation materials
   - User guide
   - Source code with comments
