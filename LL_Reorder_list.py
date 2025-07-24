# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first we need to identify the second half of the list

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second part of teh list
        second = slow.next
        prev = None
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two list

        first = head
        second = prev
        while second:
            tmp_first, tmp_second = first.next, second.next
            first.next = second
            second.next = tmp_first
            first = tmp_first
            second = tmp_second

        return head

