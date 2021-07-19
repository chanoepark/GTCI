"""
LC 141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list 
that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    slow, fast = head, head
        
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
        
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print('LinkedList has cycle:', hasCycle(head))

head.next.next.next.next.next = head.next.next
print('LinkedList has cycle:', hasCycle(head))

