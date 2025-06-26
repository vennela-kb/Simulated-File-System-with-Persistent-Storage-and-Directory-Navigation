from disk import Disk
from filesystem import FileSystem
from shell import Shell

def main():
    # Initialize the virtual disk
    disk = Disk('disk.img')
    
    # Create the file system
    fs = FileSystem(disk)
    
    # Create and run the shell
    shell = Shell(fs)
    shell.run()
    
    # Clean up
    disk.close()

if __name__ == "__main__":
    main()
