# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n + 1)

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p1] = p2
                rank[p2] += 1
            
            return True
        res = []
        for n1, n2 in edges:
            if union(n1, n2) == False:
                res.append([n1, n2])
        
        return res[-1]
        


# Time Complexity: O(E * α(V)) where E is the number of edges and V is the number of vertices. α is the Inverse Ackermann function, which grows very slowly.
# Space Complexity: O(V) for the parent and rank arrays.
# The approach uses the Union-Find (Disjoint Set Union) data structure to efficiently detect
# cycles in the graph. Each node starts as its own component, and as edges are processed,
# components are merged. If an edge connects two nodes that are already in the same component,
# it indicates a cycle, and that edge is recorded as a redundant connection. The find function
# uses path compression to optimize future queries, and the union function uses union by rank
# to keep the tree flat. The last recorded redundant connection is returned as the result.