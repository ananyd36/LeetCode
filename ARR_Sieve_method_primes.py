# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0



class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        if n < 2:
            return 0
            
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(n**0.5)+1):
            if is_prime[i]:
                start = i*i
                while start < n:
                    is_prime[start] = False
                    start+=i
        
        return sum(is_prime)

