# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

# Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

# The first letter where they differ is smaller in a than in b.
# a is a prefix of b and a.length < b.length.
# Example 1:

# Input: ["z","o"]

# Output: "zo"
# Explanation:
# From "z" and "o", we know 'z' < 'o', so return "zo".

# Example 2:

# Input: ["hrn","hrf","er","enn","rfnn"]

# Output: "hernf"
# Explanation:

# from "hrn" and "hrf", we know 'n' < 'f'
# from "hrf" and "er", we know 'h' < 'e'
# from "er" and "enn", we know get 'r' < 'n'
# from "enn" and "rfnn" we know 'e'<'r'
# so one possibile solution is "hernf"
# Constraints:

# The input words will contain characters only from lowercase 'a' to 'z'.
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100



class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def dfs(src, adj, visit, topSort):
            if src in visit:
                return
            visit.add(src)
            
            for neighbor in adj[src]:
                dfs(neighbor, adj, visit, topSort)
            topSort.append(src)
        
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(len(w1)):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

    
        
        # Step 3: DFS with cycle detection
        visiting = set()
        visited = set()
        result = []

        def dfs(c):
            if c in visiting:
                return False  # cycle detected
            if c in visited:
                return True

            visiting.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visiting.remove(c)
            visited.add(c)
            result.append(c)
            return True

        # Step 4: Run DFS on ALL nodes
        for c in adj:
            if c not in visited:
                if not dfs(c):
                    return ""

        # Step 5: Reverse topological order
        return "".join(reversed(result))


    
# Overall it had two steps:
# 1. Build the graph by comparing adjacent words to determine the order of characters.
# 2. Perform a DFS-based topological sort with cycle detection to derive the character order.