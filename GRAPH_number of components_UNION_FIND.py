# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Parent array: each node initially points to itself
        par = [i for i in range(n)]
        
        # Rank array (used here as "size" of each set)
        # Helps optimize union by attaching smaller tree under larger tree
        rank = [1] * n  

        # ----------- FIND FUNCTION -----------
        def find(n):
            # Find the root parent of node `n`
            res = n
            while res != par[res]:       # while not pointing to itself
                par[res] = par[par[res]] # path compression: point to grandparent
                res = par[res]           # move one step up
            return res

        # ----------- UNION FUNCTION -----------
        def union(n1, n2):
            # Find root parents of both nodes
            p1, p2 = find(n1), find(n2)

            # If they already belong to the same set, no union needed
            if p1 == p2:
                return 0  # means no reduction in number of components
            
            # Attach the smaller tree under the larger tree
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]  # increase size of resulting tree
            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                # If equal, attach arbitrarily and increase rank
                par[p2] = p1
                rank[p1] += 1

            return 1  # union successful, one less connected component
        
        # ----------- MAIN LOGIC -----------
        res = n  # Initially, every node is its own component
        for n1, n2 in edges:
            if union(n1, n2):  # If union merges two different components
                res -= 1       # Reduce total component count
        
        return res  # Final number of connected components
    

# Time Complexity: O(E * α(V)) where E is the number of edges and V is the number of vertices. α is the Inverse Ackermann function, which grows very slowly.
# Space Complexity: O(V) for the parent and rank arrays.
# The approach uses the Union-Find (Disjoint Set Union) data structure to efficiently manage and merge
#  connected components in the graph. Each node starts as its own component, and as edges are
# processed, components are merged. The find function uses path compression to optimize future queries,
# and the union function uses union by rank to keep the tree flat. The final count of
# connected components is derived from the number of successful unions performed.