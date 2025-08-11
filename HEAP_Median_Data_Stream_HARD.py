# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 







class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if len(self.small) > 1 + len(self.large):
            popped = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, popped)
        
        if len(self.large) > 1 + len(self.small):
            popped = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * popped)

        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            popped_small = -1 * heapq.heappop(self.small)
            popped_large = heapq.heappop(self.large)
            heapq.heappush(self.large, popped_small)
            heapq.heappush(self.small, -1*popped_large)
    


        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0] ) / 2

        

# Added explanation:
# The MedianFinder class uses two heaps: a max-heap (small) for the lower half of the numbers and a min-heap (large) for the upper half. 
# The addNum method adds a number to the appropriate heap and ensures the heaps are balanced. 
# The findMedian method returns the median based on the sizes of the heaps. 
# If the max-heap has more elements, the median is the top of the max-heap. 
# If the min-heap has more elements, the median is the top of the min-heap. 
# If both heaps are of equal size, the median is the average of the tops of both heaps.