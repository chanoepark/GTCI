"""
LC 876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, 
return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNodeImproved(head):
    # Improved solution based on LC solution
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def middleNode(head):
    # My solution
    # Fast & slow pointer where fast takes two steps and slow takes one step
    # When the fast reaches the end of the list, slow would be at the half way point thus the center
    fast, slow = head, head
    
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        
        if fast.next == None:
            # End of list
            return slow
    
    if fast.next != None:
        # Even length LinkedList
        slow = slow.next
    
    return slow


# Single node
head = Node(1)
center = middleNode(head)
print('Center of LinkedList:', center.val)

# Odd length LinkedList
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
center = middleNode(head)
print('Center of LinkedList:', center.val)

# Even length LinkedList
head.next.next.next.next.next = Node(6)
center = middleNode(head)
print('Center of LinkedList:', center.val)

