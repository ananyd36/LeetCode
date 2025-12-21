# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:

            res += matrix.pop(0)

            #Step2
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            #Step3
            if matrix:
                res+=matrix.pop()[::-1]
            
            #Step4
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        
        return res


# Explanation: You should return [1,2,3,6,9,8,7,4,5].
# The Spiral order of a matrix can be obtained by repeatedly removing the first row, then the last element of each remaining row, then the last row in 
# reverse order, and finally the first element of each remaining row in reverse order, until there are no elements left in the matrix.
