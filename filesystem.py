import time
import pickle
import os
from bitmap import Bitmap
from directory import Directory

class FileMetadata:
    def __init__(self, filename):
        self.filename = filename
        self.creation_time = time.time()
        self.last_modified_time = self.creation_time
        self.size = 0
        self.blocks = []  # List of block numbers where file data is stored
        self.block_size = 512  # Default block size

    def update_size(self, size):
        self.size = size
        self.last_modified_time = time.time()

    def add_block(self, block_num):
        self.blocks.append(block_num)

    def remove_block(self, block_num):
        if block_num in self.blocks:
            self.blocks.remove(block_num)

class FileSystem:
    def __init__(self, disk):
        self.disk = disk
        self.bitmap = Bitmap(disk, 1024)
        self.root = Directory()  # Create root directory
        self.directories = {'/': self.root}  # Store root directory
        self.current_directory = self.root
        self.metadata_file = 'fs_metadata.pkl'
        self.load_metadata()

    def load_metadata(self):
        """Load file system metadata from disk"""
        try:
            if os.path.exists(self.metadata_file):
                with open(self.metadata_file, 'rb') as f:
                    data = pickle.load(f)
                    self.directories = data['directories']
                    self.current_directory = self.directories['/']  # Always start at root
                    self.bitmap.free_blocks = set(data['free_blocks'])
                    # Reconstruct parent relationships
                    self._rebuild_directory_tree(self.directories['/'])
        except Exception as e:
            print(f"Error loading metadata: {e}")
            # Initialize with default values if loading fails
            self.directories = {'/': Directory()}
            self.current_directory = self.directories['/']
            self.bitmap.free_blocks = set(range(1024))

    def _rebuild_directory_tree(self, directory):
        """Rebuild parent-child relationships after loading from disk"""
        for name, entry in directory.entries.items():
            if isinstance(entry, Directory):
                entry.parent = directory
                self._rebuild_directory_tree(entry)

    def save_metadata(self):
        """Save file system metadata to disk"""
        try:
            data = {
                'directories': self.directories,
                'free_blocks': list(self.bitmap.free_blocks)
            }
            with open(self.metadata_file, 'wb') as f:
                pickle.dump(data, f)
        except Exception as e:
            print(f"Error saving metadata: {e}")

    def create_file(self, filename, data):
        file_metadata = FileMetadata(filename)
        current_dir = self.get_current_directory()
        
        if filename not in current_dir.entries:
            # Convert data to bytes if it's a string
            if isinstance(data, str):
                data = data.encode('utf-8')
            
            # Calculate number of blocks needed
            num_blocks = (len(data) + file_metadata.block_size - 1) // file_metadata.block_size
            
            # Allocate blocks and write data
            for i in range(num_blocks):
                block_num = self.bitmap.allocate()
                if block_num is None:
                    # Clean up allocated blocks if we run out of space
                    for block in file_metadata.blocks:
                        self.bitmap.deallocate(block)
                    print("Error: Not enough space on disk")
                    return
                
                file_metadata.add_block(block_num)
                start = i * file_metadata.block_size
                end = min((i + 1) * file_metadata.block_size, len(data))
                block_data = data[start:end].ljust(file_metadata.block_size, b'\0')
                self.disk.write_block(block_num, block_data)
            
            file_metadata.update_size(len(data))
            current_dir.entries[filename] = file_metadata
            self.save_metadata()
        else:
            print(f"Error: File {filename} already exists.")

    def read_file(self, filename):
        current_dir = self.get_current_directory()
        if filename in current_dir.entries:
            file_metadata = current_dir.entries[filename]
            data = b""
            
            # Read data from all blocks
            for block_num in file_metadata.blocks:
                block_data = self.disk.read_block(block_num)
                data += block_data
            
            # Trim padding and convert to string if it was originally a string
            data = data[:file_metadata.size]
            try:
                return data.decode('utf-8')
            except UnicodeDecodeError:
                return data
        else:
            print(f"Error: File {filename} not found.")
            return None

    def delete_file(self, filename):
        current_dir = self.get_current_directory()
        if filename in current_dir.entries:
            entry = current_dir.entries[filename]
            
            if isinstance(entry, Directory):
                # Check if directory is empty
                if entry.entries:
                    print(f"Error: Directory '{filename}' is not empty")
                    return
                # Remove directory
                del current_dir.entries[filename]
                print(f"Directory '{filename}' deleted successfully.")
            else:
                # Deallocate all blocks for file
                for block_num in entry.blocks:
                    self.bitmap.deallocate(block_num)
                
                del current_dir.entries[filename]
                print(f"File '{filename}' deleted successfully.")
            
            self.save_metadata()
        else:
            print(f"Error: '{filename}' not found.")

    def create_directory(self, dirname):
        current_dir = self.get_current_directory()
        try:
            if dirname in current_dir.entries:
                print(f"Error: Directory '{dirname}' already exists")
                return None
            new_dir = current_dir.create_directory(dirname)
            self.save_metadata()
            return new_dir
        except Exception as e:
            print(f"Error creating directory: {e}")
            return None

    def change_directory(self, path):
        """Change current directory to the specified path"""
        if path == '/':
            self.current_directory = self.directories['/']
            return

        if path.startswith('/'):
            # Absolute path
            current = self.directories['/']
            parts = path.strip('/').split('/')
        else:
            # Relative path
            current = self.current_directory
            parts = path.split('/')

        for part in parts:
            if part == '':
                continue
            elif part == '.':
                continue
            elif part == '..':
                if current.parent is not None:
                    current = current.parent
                continue
            
            next_dir = current.get_directory(part)
            if next_dir is None:
                print(f"Error: Directory '{part}' not found")
                return
            current = next_dir

        self.current_directory = current

    def list_directory(self, path='.'):
        if path == '.':
            current_dir = self.get_current_directory()
        else:
            if path.startswith('/'):
                # Handle absolute path
                parts = path.strip('/').split('/')
                current_dir = self.directories['/']
                for part in parts:
                    if part == '':
                        continue
                    current_dir = current_dir.get_directory(part)
                    if current_dir is None:
                        print(f"Error: Directory {part} not found")
                        return []
            else:
                # Handle relative path
                current_dir = self.get_current_directory()
                parts = path.split('/')
                for part in parts:
                    if part == '..':
                        if current_dir.parent:
                            current_dir = current_dir.parent
                        else:
                            print("Already at root directory")
                            return []
                    elif part != '.':
                        current_dir = current_dir.get_directory(part)
                        if current_dir is None:
                            print(f"Error: Directory {part} not found")
                            return []
        
        entries = current_dir.list_directory()
        result = []
        for entry in entries:
            if isinstance(current_dir.entries[entry], Directory):
                result.append(f"{entry}/")
            else:
                result.append(entry)
        return result

    def print_working_directory(self):
        print(f"Current directory: {self.current_directory}")

    def get_current_directory(self):
        """Get the current directory object"""
        return self.current_directory

    def help(self):
        print("""
Available Commands:
- mkdir <dirname>: Create a new directory
- cd <dirname>: Change the current working directory
- ls: List files and directories in the current directory
- pwd: Print the current working directory
- create <filename>: Create a file with data
- read <filename>: Read the content of a file
- delete <filename>: Delete a file
- help: Show this help message
- exit: Exit the program
        """)


class Directory:
    def __init__(self):
        self.entries = {}  # This stores file/directory names and their metadata or objects

    def create_directory(self, name):
        if name not in self.entries:
            self.entries[name] = Directory()
        else:
            raise Exception(f"Directory {name} already exists.")

    def get_directory(self, name):
        return self.entries.get(name)

    def list_directory(self):
        return list(self.entries.keys())


class Bitmap:
    def __init__(self, disk, block_size):
        self.disk = disk
        self.block_size = block_size
        self.free_blocks = set(range(1024))  # Let's assume there are 1024 blocks initially

    def allocate(self):
        if self.free_blocks:
            block = self.free_blocks.pop()
            return block
        else:
            print("Error: No free blocks available.")
            return None

    def deallocate(self, block):
        self.free_blocks.add(block)
