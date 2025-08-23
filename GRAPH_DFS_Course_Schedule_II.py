class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for i in range(numCourses):
            adjList[i] = []
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        cycle, visit = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:  # cycle has been detected
                return False
            if crs in visit:  # this was visited but not in the current cycle we can skip it
                return True


            cycle.add(crs)

            for pre in adjList[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        

        for crs in adjList:
            if dfs(crs) == False:
                return []
        return res
    
# Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites.
# Space Complexity: O(V + E) for the adjacency list and the visit set.
# The approach is to detect cycle because if we have a cyclical dependency between anytwo courses it would be impossible to 
# complete them. Hence we create a adjList for the problem using the course prereq input as edges of the graph and use DFS to 
# iterate through the nodes checking cycles. We are using sets to mark the nodes as visited and returning true if any node is 
# visited again. If we are able to visit all the nodes without a cycle we return the reverse of the order in which we visited the nodes.
# We return the reverse because we want to take the course only after taking all its prerequisites.
