# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, cur, k):
        while cur and k > 1:
            cur = cur.next
            k -= 1
        return cur

    def reverse(self, curHead):
        prev = None
        while curHead:
            nextNode = curHead.next
            curHead.next = prev
            prev = curHead
            curHead = nextNode
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevNode = dummy
        tmp = head

        while tmp:
            kth = self.getKth(tmp, k)
            if not kth:
                break

            nextNode = kth.next
            kth.next = None  # Detach the current k-group

            # Reverse current group
            reversedHead = self.reverse(tmp)

            # Connect previous part with reversed group
            prevNode.next = reversedHead

            # Connect end of reversed group to the next part
            tmp.next = nextNode

            # Move prevNode and tmp to the next group
            prevNode = tmp
            tmp = nextNode

        return dummy.next


# Approach: The solution uses a two-pointer technique to reverse the linked list in groups of k nodes.
# The `getKth` function finds the k-th node from the current position, and the `reverse` function reverses the linked list starting from the current head.
# The main function `reverseKGroup` iterates through the linked list, reversing each k-group and connecting them appropriately.
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1), as we are using constant extra space for pointers.
# Note: The input linked list is modified in place, and the function returns the new head