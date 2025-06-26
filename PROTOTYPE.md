# Custom File System Prototype

## Quick Start

1. Run the file system:
```bash
python main.py
```

2. Basic commands to try:
```bash
# Create a directory
mkdir documents

# Change into directory
cd documents

# Create a file
create hello.txt
# Enter some text when prompted

# List contents
ls

# Read file
read hello.txt

# Delete file
delete hello.txt

# Go back to root
cd /

# Exit
exit
```

## Implementation Details

### Core Components

1. **Virtual Disk (disk.py)**
   - Simulates physical disk with 512-byte blocks
   - Total size: 1MB (configurable)
   - Basic operations: read_block, write_block

2. **File System (filesystem.py)**
   - Manages files and directories
   - Handles block allocation
   - Tracks metadata (size, timestamps)
   - Supports persistence

3. **Directory Structure (directory.py)**
   - Tree-based organization
   - Supports absolute/relative paths
   - Parent-child relationships

4. **Block Allocation (bitmap.py)**
   - Tracks free/used blocks
   - Supports dynamic allocation
   - Efficient space management

### Key Features

1. **File Operations**
   - Create files with content
   - Read file contents
   - Delete files
   - Track file metadata

2. **Directory Management**
   - Create directories
   - Navigate directory tree
   - List directory contents
   - Support for paths

3. **Persistence**
   - Saves state between sessions
   - Stores metadata in fs_metadata.pkl
   - Maintains disk image

## Technical Specifications

- Block Size: 512 bytes
- Disk Size: 1MB
- Maximum Files: Limited by available blocks
- Maximum File Size: Limited by available blocks
- Directory Depth: Unlimited

## Error Handling

Common errors and solutions:
- "File already exists": Choose a different name
- "Directory not found": Check path spelling
- "No free blocks": Delete some files
- "File not found": Check filename and path

## Performance Considerations

- Block allocation is O(1)
- Directory lookup is O(n) where n is path depth
- File operations are O(1) for metadata, O(n) for data where n is number of blocks

## Testing

To test the file system:
1. Create multiple directories
2. Create files of different sizes
3. Navigate through directories
4. Read/delete files
5. Exit and restart to verify persistence 