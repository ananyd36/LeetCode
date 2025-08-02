class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        res, visited = set(), set()

        def dfs(row, col, node, word):
            if (min(row, col) < 0 or 
            row==len(board) or col == len(board[0]) or 
            (row, col) in visited or 
            board[row][col] not in node.children):
                return

            visited.add((row,col))
            node = node.children[board[row][col]]
            word+=board[row][col]
            
            if node.word:
                res.add(word)
            
            dfs(row +1, col, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)


            visited.remove((row,col))

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, trie.root, "")
        
        return list(res)

        

# Intuition
# If you havent solved Word Search, I would highly recommend solving that before we dive deep in this. Assuming you are familiar with the problem, initial way of doing this problem can be using a matrix DFS apprach for each word and checking if its present or not. But it will be really inefficient.
# For every word and applying DFS in 4 directions -> 4 ^ mn and then this is done for each elemnet in the matrix mn(4 ^ mn) - > now this is done for each word in the list L(mn(4 ^ mn)) where L is the length of word list.

# Approach
# Since isntead of directly checking all the elements in the matrix if a word can be build we can check if the element at the location of the matrix is a prefix of any possible word from the list, We can achieve this using a Trie and built a trie of the list of words, if present we can apply DFS to check if it leads to a word in all 4 directions

# Complexity
# Time complexity:
# For Building a Trie, if we assume L is the longest word in the list and W is the number of words, A trie can be build in O(W*L)

# DFS traversal:
# For DFS the maximum we can traverse is till the length of the longest word, else if we encounter a letter not in the node's children we break out of it. Hence worst case we will take O(4^L). Now we perform this for each element in the matrix hence O(4^L * (m*n))

# Combining we will get O(4^L * (mn)) + O(WL).

# Space complexity:
# Space is consumed by the Trie, the recursion stack for the DFS, and the storage for the results.

# Trie Storage
# The space required to store the Trie is proportional to the total number of characters across all words in the input list.

# Complexity: O(W×L)

# Recursion Stack
# The maximum depth of the dfs recursive calls is limited by the length of the longest word, L.

# Complexity: O(L)

# Overall Space Complexity

# The dominant factor in space usage is the Trie itself.

# Total Space=O(W×L)



# Matrix DFS Approach
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(row, col, i):
            # we check if we have reached the end of the word
            if i == len(word):
                return True

            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited or board[row][col] != word[i]:
                return False

            visited.add((row, col))

            
            res = (
                dfs(row, col + 1, i + 1) or 
                dfs(row, col - 1, i + 1) or 
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1)
            )

            visited.remove((row, col))

            return res

        # Start DFS from every cell that matches word[0]
        result = []
        for word in words:
            visited = set()
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == word[0] and dfs(i, j, 0):
                        result.append(word)

        return result








