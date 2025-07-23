# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node

        # Dummy nodes
        self.left = Node(0, 0)  # LRU end
        self.right = Node(0, 0)  # MRU end

        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert node at MRU position (just before right)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            # remove LRU from list and hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]




# Approach: The LRUCache uses a doubly linked list to maintain the order of usage and a hashmap for O(1) access to nodes.
# The `get` method retrieves the value for a key and moves the node to the MRU position.
# The `put` method adds a new key-value pair or updates an existing one, moving the node to the MRU position. If the cache exceeds its capacity, it removes the LRU node.
# Time Complexity: O(1) for both `get` and `put` operations.
# Space Complexity: O(capacity) for storing the nodes in the cache.
# Note: The cache maintains the order of usage without modifying the input data structure, and it uses constant extra space for the linked list and hashmap.
# The linked list is used to track the order of usage, with the left dummy node representing the least recently used end and the right dummy node representing the most recently used end.  
# The `remove` method detaches a node from the linked list, and the `insert` method adds a node just before the right dummy node.
# The `get` method checks if the key exists, retrieves the node, removes it from its current position, and reinserts it at the MRU position.
# The `put` method checks if the key already exists, removes it if it does,
# creates a new node, adds it to the cache and linked list, and checks if the
# cache exceeds its capacity. If it does, it removes the LRU node from both the linked list and the hashmap.
# The cache is designed to efficiently handle the constraints of an LRU cache, ensuring that both `get` and `put` operations run in O(1) time.
