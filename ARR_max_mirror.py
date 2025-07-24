# We'll say that a "mirror" section in an array is a group of contiguous elements such that somewhere in the array, the same group appears in reverse order. 
# For example, the largest mirror section in {1, 2, 3, 8, 9, 3, 2, 1} is length 3 (the {1, 2, 3} part). Return the size of the largest mirror section found in the given array.

# maxMirror([1, 2, 3, 8, 9, 3, 2, 1]) → 3
# maxMirror([1, 2, 1, 4]) → 3
# maxMirror([7, 1, 2, 9, 7, 2, 1]) → 2

def maxMirror(arr):



    # Initialize the maximum length of the mirror section to 0.
    max_length = 0
    
    # Outer loop: iterate through each element in the array.
    for i in range(len(arr)):
        # Inner loop: iterate backwards through the array to find a mirror.
        for j in range(len(arr), 0, -1):
            # Length of the current mirror section.
            length = 0
            
            # While loop to explore the potential mirror section.
            # It also checks the boundaries to avoid index out of range.
            while i + length < len(arr) and j - length - 1 >= 0 and arr[i + length] == arr[j - length - 1]:
                length += 1  # Increment the length if the current elements match.
            
            # Update the maximum length found so far.
            max_length = max(max_length, length)
    
    # Return the maximum length of the mirror section found.
    return max_length


