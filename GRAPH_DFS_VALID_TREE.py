# Detecting cycle in an undirected graph using DFS



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}

        for i in range(n):
            adjList[i] = []
        
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visit, cycle = set(), set()

        def dfs(node, parent):
            if node in cycle:
                return False
            
            cycle.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True
        
        return dfs(0, -1) and len(visit) == n
    


# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V + E) for the adjacency list and the visit and cycle sets.
# The approach is to detect cycle because if we have a cyclical dependency between any two nodes it would be impossible to 
# have a valid tree. Hence we create a adjList for the problem using the edges input as edges of the graph and use DFS to 
# iterate through the nodes checking cycles. We are using sets to mark the nodes as visited and returning true if any node is 
# visited again. We also need to check if all nodes are connected hence we check if the length of the visit set is equal to n at the end.
# We return the result of the DFS starting from node 0 and parent -1 (as there is no parent for the root node).