
# ### Intuition

# The problem requires two main operations: adding words and searching for them. The search is special because it includes a `.` wildcard that can match any single character.

# A simple hash set could handle `addWord` and exact searches efficiently. However, it would struggle with the wildcard. Searching for "b.d" would force us to iterate through every word in our dictionary to see if it matches the pattern, which is very slow.

# This need for efficient prefix and pattern matching strongly suggests a **Trie (Prefix Tree)**. A Trie stores words character by character, where each node represents a prefix. A search for "cat" involves traversing the path `c -> a -> t`.

# The wildcard `.` fits this model perfectly. When we encounter a `.` during a search, it simply means we don't know which path to take next. So, we must explore **all possible paths** from our current node. This exploratory behavior is a natural fit for a Depth-First Search (DFS) or backtracking algorithm.

# ### Approach

# The solution uses a Trie data structure, with a recursive DFS method for searching.

# 1.  **TrieNode Structure**: Each node in our Trie contains:

#       * `children`: A dictionary mapping a character to a child `TrieNode`.
#       * `word`: A boolean flag that is `True` only if the path from the root to this node represents a complete word in our dictionary.

# 2.  **`addWord(word)`**: This function is straightforward. We start at the root and iterate through each character of the word. For each character, we traverse to the corresponding child node. If a child node for a character doesn't exist, we create one. After iterating through all characters, we mark the final node's `word` flag as `True`.

# 3.  **`search(word)`**: This is the core of the solution, implemented with a recursive helper function `dfs(j, root)` where `j` is the current character index in the word and `root` is the current Trie node.

#       * **Base Case**: The recursion ends when we've processed the entire search word. The search is successful only if the final node's `word` flag is `True`.
#       * **Recursive Step**: We inspect the character `word[j]`.
#           * If it's a normal letter, we check if a corresponding child exists in the current node. If not, the word doesn't exist. If it does, we continue the search from that child node with the next character (`j + 1`).
#           * If it's a `.` wildcard, we must try every possible path. We iterate through all of the current node's children. For each `child`, we launch a new recursive search `dfs(j + 1, child)`. If **any** of these recursive calls return `True`, it means we've found a match, and we can immediately return `True`. If we try all children and none result in a match, we return `False`.

# ### Complexity

# Let $N$ be the number of words in the dictionary and $L$ be the maximum length of a word.

#   - **Time complexity:**

#       * `addWord`: To add a word, we iterate through its characters once. The complexity is proportional to the length of the word, so it's $O(L)$.
#       * `search`: For a word without wildcards, the search is also $O(L)$. For a word with wildcards, in the worst-case scenario (e.g., searching for "....."), we might have to explore every node in the Trie. The total number of nodes is at most $N \\cdot L$. Therefore, the worst-case time complexity is $O(N \\cdot L)$.

#   - **Space complexity:**

#       * `addWord`: Adding a word of length $L$ could, in the worst case, add $L$ new nodes to the Trie. This requires $O(L)$ space. The total space used by the Trie is $O(N \\cdot L)$.
#       * `search`: The space is determined by the maximum depth of the recursion stack, which is equal to the length of the word being searched. This is $O(L)$.

# ### Code

class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes for each character.
        self.children = {}
        # Boolean to mark if the node represents the end of a complete word.
        self.word = False


class WordDictionary:
    def __init__(self):
        # The root of the Trie, an empty node.
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Adds a word to the Trie data structure."""
        cur = self.root
        for c in word:
            # If the character path doesn't exist, create it.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node.
            cur = cur.children[c]
        # Mark the end of the word.
        cur.word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie. The word can contain '.' as a wildcard
        to match any character.
        """
        def dfs(j, root):
            """
            Performs a depth-first search on the Trie.
            j: current index in the search word.
            root: current TrieNode to search from.
            """
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # Wildcard: try every possible path from this node.
                    for child in cur.children.values():
                        # If any path leads to a solution, return True.
                        if dfs(i + 1, child):
                            return True
                    # If no child path works, this path is a dead end.
                    return False
                else:
                    # Normal character: check if the path exists.
                    if c not in cur.children:
                        return False
                    # Move to the next node in the path.
                    cur = cur.children[c]
            
            # After iterating through the word, check if it's a complete word.
            return cur.word

        return dfs(0, self.root)
