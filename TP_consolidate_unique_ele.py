# In this task, you are provided with a list of integers named 'nums', which is ordered in a non-decreasing sequence.
# Your objective is to reorganize 'nums' in-place to ensure that each unique number appears only once, preserving their original order.
# Consequently, you are required to output the count of these unique numbers found in 'nums'.
 
# Perform your task under the following constraints and guidelines:
# - Directly modify the 'nums' array so that the initial portion up to 'k' (the return value) contains all the unique numbers in their original sequence.
# The content beyond 'k' in the array is inconsequential.
# - Your primary output should be 'k', the total count of unique elements within 'nums'.
 
# For instance:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# In this example, the method would result in 'k' being 2, signifying the presence of two unique elements which are 1 and 2, and 'nums' being modified to contain these two elements at the start.
 
# Another example:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Here, 'k' is 5, indicating five unique numbers (0, 1, 2, 3, 4) placed at the beginning of 'nums'.
# The positions after 'k' are irrelevant.
 
# Constraints:
# - The length of 'nums' is at least 1 and at most 3 * 10^4.
# - Each element in 'nums' can be any integer between -100 and 100.
# - 'nums' is given in a non-decreasing order.

def removeDuplicates(nums):
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j+=1
    return j

#approach:
# 1. Initialize a pointer j at 1, as the first element is always unique.
# 2. Iterate through the list starting from the second element (index 1).
# 3. For each element, check if it is different from the previous element.
# 4. If it is different, assign the current element to nums[j] and increment j.
# 5. Continue this process until the end of the list.
# 6. Return j, which represents the count of unique elements.
# Time Complexity: O(n), where n is the length of the input list 'nums'.
# Space Complexity: O(1), as we are modifying the list in place and not using any additional data structures.