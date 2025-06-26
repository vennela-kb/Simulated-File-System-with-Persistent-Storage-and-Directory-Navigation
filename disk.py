import os

class Disk:
    def __init__(self, filename, block_size=512, disk_size=1024 * 1024):
        self.filename = filename
        self.block_size = block_size
        self.disk_size = disk_size
        self.num_blocks = disk_size // block_size
        self.disk = open(filename, 'wb+')

    def read_block(self, block_num):
        """Read a block from the disk"""
        self.disk.seek(block_num * self.block_size)
        return self.disk.read(self.block_size)

    def write_block(self, block_num, data):
        """Write a block to the disk"""
        self.disk.seek(block_num * self.block_size)
        self.disk.write(data)

    def close(self):
        """Close the disk file"""
        self.disk.close()

# Example usage
disk = Disk('disk.img')
disk.write_block(0, b'Hello, World!')
print(disk.read_block(0))
disk.close()
