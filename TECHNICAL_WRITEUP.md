# Technical Write-up: Custom File System Design

## Data Structures and Design Choices

### 1. Block Allocation System
- **Structure**: Bitmap-based allocation
- **Advantages**:
  - O(1) allocation/deallocation
  - Simple and efficient space tracking
  - Easy to implement and maintain
  - Low memory overhead
- **Comparison with Traditional Systems**:
  - FAT: Uses linked lists, which can fragment
  - ext: Uses bitmaps but with more complex structures
  - Btrfs: Uses B-trees for more advanced features

### 2. Directory Structure
- **Structure**: Tree-based with parent-child relationships
- **Advantages**:
  - Natural representation of hierarchical paths
  - Efficient navigation
  - Easy to implement relative paths
  - Simple to maintain
- **Comparison with Traditional Systems**:
  - FAT: Flat directory structure
  - ext: Similar tree structure but more complex
  - Btrfs: Advanced B-tree with more features

### 3. File Metadata
- **Structure**: Object-based with block pointers
- **Advantages**:
  - Direct access to file blocks
  - Easy to track file size and timestamps
  - Simple to implement persistence
- **Comparison with Traditional Systems**:
  - FAT: Limited metadata
  - ext: More comprehensive metadata
  - Btrfs: Advanced metadata with checksums

## Advantages Over Traditional Systems

1. **Simplicity and Efficiency**
   - Our design is simpler than FAT/ext/Btrfs while maintaining core functionality
   - Easier to understand and maintain
   - Lower overhead for basic operations

2. **Flexible Block Allocation**
   - More efficient than FAT's linked lists
   - Simpler than ext's complex block allocation
   - Better suited for educational purposes

3. **Clean Directory Structure**
   - More intuitive than FAT's flat structure
   - Easier to implement than ext's complex directory system
   - Better suited for learning file system concepts

4. **Persistence Implementation**
   - Simple and effective metadata storage
   - Easy to understand and modify
   - Good balance between functionality and complexity

## Limitations and Future Improvements

1. **Current Limitations**
   - No file permissions
   - No symbolic links
   - No journaling
   - Limited error recovery

2. **Planned Improvements**
   - Add file permissions system
   - Implement symbolic links
   - Add journaling for crash recovery
   - Implement file system checks

## Conclusion

Our file system design provides a good balance between functionality and simplicity. While it may not have all the features of production file systems like FAT, ext, or Btrfs, it serves as an excellent educational tool and demonstrates the core concepts of file system design effectively.

The design choices were made with the following goals in mind:
1. Educational value
2. Easy to understand and modify
3. Demonstrates core file system concepts
4. Maintains good performance for basic operations 