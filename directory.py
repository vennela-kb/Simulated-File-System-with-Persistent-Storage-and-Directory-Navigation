import os

class Directory:
    def __init__(self, name='', parent=None):
        self.name = name
        self.parent = parent
        self.entries = {}  # Maps names to either FileMetadata or Directory objects
        self.path = self._calculate_path()

    def _calculate_path(self):
        """Calculate the full path of this directory"""
        if self.parent is None or self.name == '':
            return '/'
        elif self.parent.path == '/':
            return '/' + self.name
        else:
            return os.path.join(self.parent.path, self.name)

    def create_directory(self, name):
        """Create a new directory with the given name"""
        if name not in self.entries:
            new_dir = Directory(name, self)
            self.entries[name] = new_dir
            return new_dir
        else:
            raise Exception(f"Directory {name} already exists.")

    def get_directory(self, name):
        """Get a directory by name"""
        if name == '..':
            return self.parent
        elif name == '.':
            return self
        return self.entries.get(name)

    def list_directory(self):
        """List all entries in this directory"""
        return list(self.entries.keys())

    def get_full_path(self, name):
        """Get the full path for an entry in this directory"""
        if self.path == '/':
            return '/' + name
        return os.path.join(self.path, name)

    def __getstate__(self):
        """Custom serialization to avoid circular references"""
        state = self.__dict__.copy()
        # Don't serialize the parent reference
        state['parent'] = None
        return state

    def __setstate__(self, state):
        """Custom deserialization"""
        self.__dict__.update(state)
        # Parent will be set when reconstructing the directory tree
        self.parent = None

    def create_file(self, filename, blocks):
        """Create a file with the specified blocks"""
        self.entries[filename] = blocks

    def get_file(self, filename):
        """Get the blocks associated with a file"""
        return self.entries.get(filename)
