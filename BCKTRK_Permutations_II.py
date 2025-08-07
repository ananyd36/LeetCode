# Imagine you are given a bag of number tiles where some numbers may be repeated.
# Your task is to construct all distinct sequences that can be made with these tiles, ensuring no sequence is repeated.
# The order in which the tiles are arranged matters and introduces a new unique sequence unless it matches an already created sequence.
# For example, given a set of tiles [1,1,2], the unique sequences you can arrange are [[1,1,2], [1,2,1], [2,1,1]].
# For a set [1,2,3], the sequences include [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
# Your solution should be able to handle a set of up to 8 tiles, with each number ranging from -10 to 10.
 
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
 
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

def uniqueSequences(nums):
    res= []
    nums.sort() #we have to sort for the duplicate logic to work
    used = [False]* len(nums)
    def permute(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:    # if the element on the index is True we skip it, means. visited
                continue
            
            if i > 0 and nums[i] == nums[i-1] and not used[i]:
                continue    # it means that we have include the i-1 and algo has bactracked to i now hence we must skip the ith

            path.append(nums[i])
            used[i] = True
            permute(path)
            path.pop()
            used[i] = False

    
    permute([])
    return res