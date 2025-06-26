class Bitmap:
    def __init__(self, disk, num_blocks):
        self.disk = disk
        self.num_blocks = num_blocks
        self.bitmap = [0] * num_blocks  # 0: free, 1: used

    def allocate_block(self):
        """Find the first free block and allocate it"""
        for i in range(self.num_blocks):
            if self.bitmap[i] == 0:
                self.bitmap[i] = 1
                return i
        return -1  # No free block found

    def deallocate_block(self, block_num):
        """Mark a block as free"""
        self.bitmap[block_num] = 0

    def write_bitmap(self):
        """Write the bitmap to the disk"""
        for i in range(self.num_blocks):
            self.disk.write_block(i, bytes([self.bitmap[i]]))
