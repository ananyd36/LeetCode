class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()




# Example usageif __name__ == "__main__":
    ll = LinkedList()
    ll.insertEnd(1)
    ll.insertEnd(2)
    ll.insertEnd(3)
    ll.print()  # Output: 1 -> 2 -> 3 ->
    ll.remove(1)
    ll.print()  # Output: 1 -> 3 ->
    ll.remove(0)
    ll.print()  # Output: 3 ->
    ll.remove(0)
    ll.print()  # Output: (empty list)
    ll.remove(0)  # Attempt to remove from an empty list, should not raise an error
    ll.print()  # Output: (empty list)
    ll.insertEnd(4)
    ll.print()  # Output: 4 ->
    ll.remove(0)
    ll.print()  # Output: (empty list)