# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return 

        dummy = ListNode(0, head)

        fast = slow =  dummy

        for _ in range(n):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next

        