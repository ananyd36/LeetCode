# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]



# Solution:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        res = []
        for j in range(k):
            max_value = max(freq.values())
            max_key = [key for key, value in freq.items() if value==max_value]
            res.append(max_key[0])
            del(freq[max_key[0]])
        return sorted(res)
    

# Approach:
# 1. Create a frequency dictionary to count the occurrences of each element in the array.
# 2. Initialize an empty list to store the k most frequent elements.
# 3. Use a loop to find the maximum value in the frequency dictionary and its corresponding key.
# 4. Append the key to the result list and delete it from the frequency dictionary.
# 5. Repeat the process k times to get the k most frequent elements.
# 6. Return the result list sorted in ascending order.
# Time Complexity: O(n*k), where n is the number of elements in the array and k is the number of most frequent elements to find.
# Space Complexity: O(n), where n is the number of unique elements in the array.
# Note: The above approach is not optimal. A better approach would be to use a heap to find the k most frequent elements in O(n log k) time.
# Optimized Approach:
from collections import Counter
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, value in freq.items():
            heappush(heap, (value, key))
            if len(heap) > k:
                heappop(heap)
        return [heappop(heap)[1] for _ in range(k)][::-1]
# Approach:
# 1. Use the Counter class from the collections module to count the occurrences of each element in the array.
# 2. Initialize an empty heap to store the k most frequent elements.
# 3. Iterate through the frequency dictionary and push each element into the heap.
# 4. If the size of the heap exceeds k, pop the smallest element from the heap.
# 5. After processing all elements, pop the elements from the heap to get the k most frequent elements.
# 6. Return the result list in reverse order to get the most frequent elements first.
# Time Complexity: O(n log k), where n is the number of elements in the array and k is the number of most frequent elements to find.
# Space Complexity: O(n), where n is the number of unique elements in the array.
# Note: The optimized approach is more efficient than the previous approach, especially for large arrays.
# The use of a heap allows us to maintain the k most frequent elements in O(log k) time for each insertion and deletion.
# This makes the overall time complexity O(n log k), which is much better than O(n*k) for large arrays.
# The space complexity remains O(n) due to the storage of the frequency dictionary and the heap.
# The optimized approach is the preferred solution for this problem, as it is more efficient and scalable for larger inputs.