Absolutely! Let's break down how the `countPrefix` function works and **how the prefix counting is stored during Trie construction**.

---

### 🔍 Goal:

You want to find **how many words** in the Trie **start with a given prefix**.

To do this efficiently, each node in the Trie **keeps track of how many words pass through it** — this is done using the `prefix_count` attribute.

---

### 📦 During Insertion (`insert` method):

Here’s the key idea:

* For each character `c` in the word, as we go deeper in the Trie:

  * If the character doesn't exist in the current node’s children, we create a new `TrieNode`.
  * We **increment `prefix_count`** for that node to indicate one more word passes through this prefix.

#### Example:

Insert `"apple"` and `"app"` into the Trie.

* After `"app"`:

  ```
  root
   └─ a (prefix_count = 2)
       └─ p (prefix_count = 2)
           └─ p (prefix_count = 2)
  ```
* After `"apple"`:

  ```
           └─ l (prefix_count = 1)
               └─ e (prefix_count = 1)
  ```

So `"app"` has `prefix_count = 2`, because both `"app"` and `"apple"` pass through it.

---

### ✅ Now `countPrefix(prefix)` does:

```python
def countPrefix(self, prefix: str) -> int:
    node = self.root
    for c in prefix:
        if c not in node.children:
            return 0  # No words with this prefix
        node = node.children[c]
    return node.prefix_count  # ✅ Number of words with the prefix
```

---

### 🔁 Walkthrough:

Let’s say you're querying `countPrefix("app")`.

* Traverse the Trie along `'a'`, `'p'`, `'p'`.
* At each step, move deeper into the child node.
* At the last `'p'`, return `node.prefix_count`.

This gives you the **number of words that share `"app"` as a prefix**.

---

### 🧠 Recap:

* Each node stores how many words have passed through it (`prefix_count`).
* During insert, you **increment `prefix_count`** as you move down.
* During prefix search, you **just return `prefix_count`** at the last character node.


```python3 []
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count+=1
        curr.word = True
        
        

    def countPrefix(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count
        
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.countPrefix(pref)
        
        


```
