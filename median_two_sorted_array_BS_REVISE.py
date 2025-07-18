# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in 
# O(log(m+n)) time.

# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:

# Input: nums1 = [1,3], nums2 = [2,4]

# Output: 2.5
# Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

# Approach
# 1. Ensure that nums1 is the smaller array.
# 2. Use binary search on the smaller array (nums1) to find the correct partition.
# 3. Calculate the indices for the partition in both arrays.
# 4. Compare the elements around the partition to ensure they are correctly ordered.
# 5. If the partition is valid, calculate the median based on the total number of elements.
# 6. If the partition is not valid, adjust the binary search bounds accordingly.
# Time Complexity: O(log(min(m, n))), where m and n are the lengths of nums1 and nums2 respectively.
# Space Complexity: O(1), as we are using a constant amount of space for variables. 