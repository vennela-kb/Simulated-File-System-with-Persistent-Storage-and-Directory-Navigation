class Shell:
    def __init__(self, filesystem):
        self.fs = filesystem

    def run(self):
        print("Welcome to the Custom File System Shell!")
        print("Type 'help' for available commands")
        
        while True:
            try:
                # Get the current directory path
                current_path = self.fs.current_directory.path if hasattr(self.fs.current_directory, 'path') else '/'
                
                # Read the command from the user
                command = input(f"{current_path}> ").strip()

                # Exit the shell if user types 'exit'
                if command == "exit":
                    break

                # Help command
                elif command == "help":
                    self.fs.help()

                # Create file command
                elif command.startswith("create "):
                    filename = command.split(" ", 1)[1]
                    data = input(f"Enter data to write to {filename}: ")
                    self.fs.create_file(filename, data)
                    print(f"File '{filename}' created successfully.")

                # Read file command
                elif command.startswith("read "):
                    filename = command.split(" ", 1)[1]
                    content = self.fs.read_file(filename)
                    if content:
                        print(f"Contents of {filename}:")
                        print(content)

                # Delete file/directory command
                elif command.startswith("delete "):
                    name = command.split(" ", 1)[1]
                    self.fs.delete_file(name)

                # List directory contents
                elif command.startswith("ls"):
                    path = command.split(" ", 1)[1] if len(command.split()) > 1 else "."
                    files = self.fs.list_directory(path)
                    if files:
                        print("Files and directories:")
                        for file in sorted(files):
                            print(file)
                    else:
                        print("No files or directories found.")

                # Make directory command
                elif command.startswith("mkdir "):
                    dirname = command.split(" ", 1)[1]
                    self.fs.create_directory(dirname)
                    print(f"Directory '{dirname}' created successfully.")

                # Change directory command
                elif command.startswith("cd "):
                    dirname = command.split(" ", 1)[1]
                    self.fs.change_directory(dirname)

                # Print working directory
                elif command == "pwd":
                    current_path = self.fs.current_directory.path if hasattr(self.fs.current_directory, 'path') else '/'
                    print(f"Current directory: {current_path}")

                # Clear screen
                elif command == "clear":
                    print("\033[H\033[J", end="")

                # Unknown command
                else:
                    print("Unknown command. Type 'help' for available commands.")

            except Exception as e:
                print(f"Error: {e}")

    def help(self):
        print("""
Available Commands:
- mkdir <dirname>: Create a new directory
- cd <dirname>: Change the current working directory (supports absolute and relative paths)
- ls [path]: List files and directories in the current or specified directory
- pwd: Print the current working directory
- create <filename>: Create a file with data
- read <filename>: Read the content of a file
- delete <filename>: Delete a file
- clear: Clear the screen
- help: Show this help message
- exit: Exit the program
        """)

