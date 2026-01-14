# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]



# Solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] +=1
            res[tuple(count)].append(s) # dictionary counts must be hashable , list are not hashable but tuples are hashable, also, list are mutable and mutable objects cannot be used as dictionary keys.
        
        return res.values()

# Approach
# 1. Create an empty dictionary called res.
# 2. Iterate through the list strs.
# 3. For each string, create a list called count of length 26 initialized to 0.
# 4. For each character in the string, increment the corresponding index in the count list.
# 5. Convert the count list to a tuple and use it as a key in the dictionary res.
# 6. Append the string to the list corresponding to the key in the dictionary.
# 7. Return the values of the dictionary as a list of lists.
# Time complexity: O(nk)
# Space complexity: O(nk)
# The time complexity of this solution is O(nk) because we need to iterate through the entire list of strings and for each string, we need to iterate through its characters.
# The space complexity is O(nk) because we need to store the dictionary of lists, where n is the number of strings and k is the maximum length of a string.
# The defaultdict is a subclass of the built-in dict class. It overrides one method to provide a default value for a nonexistent key, which is specified when the defaultdict is created.
# The tuple() function creates a tuple object, which is an immutable sequence type. It is used here to create a hashable key for the dictionary.
# The ord() function returns the Unicode code point of a character. It is used here to convert a character to its corresponding index in the count list.