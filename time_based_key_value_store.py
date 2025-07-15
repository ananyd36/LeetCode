# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar"

class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        else:
            nums = self.timeMap[key]

            left, right = 0, len(nums) - 1
            res = ""

            while left<=right:
                mid = (left + right) // 2
                if nums[mid][1] > timestamp:
                    right-=1
                else:
                    left+=1
                    res = nums[mid][0]
            return res

                    

# The above code defines a class `TimeMap` that implements a time-based key-value store.
# The class has two methods: `set` and `get`.
# The `__init__` method initializes an empty dictionary `timeMap` to store the key-value pairs along with their timestamps.
# The `set` method takes a key, value, and timestamp as arguments and stores the value along with the timestamp in a list associated with the key in `timeMap`.
# If the key does not exist in `timeMap`, it initializes an empty list for that key.
# The `get` method takes a key and a timestamp as arguments and retrieves the value associated with the key at the largest timestamp that is less than or equal to the given timestamp.
# It uses a binary search approach to find the appropriate value efficiently.
# If the key does not exist in `timeMap`, it returns an empty string.
# The time complexity for the `set` method is O(1) for inserting a new value, and for the `get` method, it is O(log n) due to the binary search.
# The space complexity is O(n) where n is the number of key-value pairs stored in the `timeMap` dictionary.
# This implementation allows for efficient storage and retrieval of values based on timestamps, making it suitable for scenarios where time-based data needs to be managed.