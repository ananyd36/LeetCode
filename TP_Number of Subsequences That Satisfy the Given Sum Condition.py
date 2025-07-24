# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
# Example 2:

# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
# Example 3:

# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).
 

def countValidSubsequences(nums, target):

    # First, sort the input array. This allows us to easily find minimum and maximum
    # values of subsequences by simply considering the ends of the array.
    nums.sort()
    
    # Initialize two pointers for the two ends of the array.
    left, right = 0, len(nums) - 1
    
    # Initialize a counter to keep track of the number of valid subsequences.
    count = 0
    
    # The modulo value as per the problem statement to prevent integer overflow.
    mod = 10 ** 9 + 7
    
    # Iterate through the array until the left pointer exceeds the right pointer.
    while left <= right:
        # If the sum of the current minimum and maximum elements is greater than the target,
        # it means we cannot include the current maximum (right-most element) in our subsequence
        # because adding any other element will only increase the sum. Thus, we move the right
        # pointer to the left to try with a smaller maximum value.
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            # If the current minimum and maximum sum is within the target, all subsets formed
            # with the current minimum and elements up to the current maximum are valid.
            # The number of such subsets is 2^(right-left), since for each element between left
            # and right (inclusive of left, exclusive of right), we can choose to include it or not.
            # This is why we use the power of 2.
            #
            # We use modulus operation to ensure the result stays within the integer limits defined
            # in the problem statement.
            count += pow(2, right - left, mod)
            
            # Move the left pointer to the right to try with a larger minimum value, since we've
            # accounted for all valid subsequences with the current minimum.
            left += 1
    
    # Return the total count of valid subsequences modulo 10^9 + 7, to ensure the final result
    # is within the integer limit.
    return count % mod