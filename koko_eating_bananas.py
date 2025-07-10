# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)
            
            if totalTime <= h:
                return speed
            speed += 1
        return speed
    

#Approach:# 1. Initialize the eating speed to 1.
# 2. Use a while loop to continuously check if Koko can finish eating all the bananas within the given hours `h`.
## 3. For each speed, calculate the total time taken to eat all the bananas:
##    - For each pile, calculate the time taken to eat that pile using `math.ceil(pile / speed)`.
##    - Sum up the time for all piles to get `totalTime`.
# 4. If `totalTime` is less than or equal to `h`, return the current speed as the minimum eating speed.
# 5. If not, increment the speed by 1 and repeat the process until a valid speed is found.
# 6. The function will return the minimum speed at which Koko can finish eating all the bananas within the given hours.


import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # i want to find k and k will always be in between 1 and k
        # using binary search i can start from this extreme and work towards the soln

        l,r  = 1, max(piles)

        while l <= r:
            k = (l+r) // 2
            time = 0
            for pile in piles:
                time += ceil(pile/k)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    

# Approach:# 1. Initialize the left pointer `l` to 1 and the right pointer `r` to the maximum value in `piles`.
# 2. Use a while loop to perform binary search until `l` is less than or equal to `r`.
# 3. Calculate the mid-point `k` as the average of `l` and `r`.
# 4. Initialize a variable `time` to 0 to keep track of the total time taken to eat the bananas.
# 5. For each pile in `piles`, calculate the time taken to eat that pile using `ceil(pile / k)` and add it to `time`.
# 6. If `time` is less than or equal to `h`, it means Koko can finish eating within the given hours, so store `k` as `res` and move the right pointer `r` to `k - 1` to search for a potentially smaller valid speed.
# 7. If `time` is greater than `h`, it means Koko needs a larger speed, so move the left pointer `l` to `k + 1` to search for a larger speed.
# 8. The loop continues until the left pointer exceeds the right pointer.
# 9. Finally, return the result `res`, which is the minimum eating speed
# that allows Koko to finish eating all the bananas within the given hours.
## The time complexity of this solution is O(n log m), where n is the number of piles
# and m is the maximum number of bananas in a pile. The space complexity is O(1) since we are using a constant amount of extra space.   