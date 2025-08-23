# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for i in range(numCourses):
            adjList[i] = []
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if adjList[crs] == []:
                return True
            
            visit.add(crs)

            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            adjList[crs] = []
            return True
        
        # because the graph can be not connected.
        for crs in adjList:
            if not dfs(crs):
                return False
        return True
        
# Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites.
# Space Complexity: O(V + E) for the adjacency list and the visit set.

# The approach is to detect cycle because if we have a cyclical dependency between anytwo courses it would be impossible to 
# complete them. Hence we create a adjList for the problem using the course prereq input as edges of the graph and use DFS to 
# iterate through the nodes checking cycles. We are using sets to mark the nodes as visited and returning true if any node is 
# visited again.