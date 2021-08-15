"""
LC 206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self):
        temp = self
        while temp is not None:
            print(temp.val, end=' ')
            temp = temp.next
        print()


def reverseListFinalIterative(head):
    # Cleaner iterative solution
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def reverseList(head):
    # My iterative solution
    if head is None:
        return head
    
    curr = head.next
    prev = head
    head.next = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev


def reverseListRecursive(head):
    # My recursive solution
    newHead = head
    if head is not None:
        newHead = reverseListRecursiveHelper(head.next, head)
        head.next = None
    return newHead


def reverseListRecursiveHelper(curr, prev):
    if curr is None:
        return prev
    head = reverseListRecursiveHelper(curr.next, curr)
    head.next = prev
    return head


# Even length list
head = Node(2)
head.next = Node(4)
print('Nodes of original list are: ', end='')
head.printList()
result = reverseList(head)
print('Nodes of iteratively reversed list are: ', end='')
result.printList()
print()

# Even length list
head = Node(2)
head.next = Node(4)
print('Nodes of original list are: ', end='')
head.printList()
result = reverseListRecursive(head)
print('Nodes of recursively reversed list are: ', end='')
result.printList()
print()

# Odd length list
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
print('Nodes of original list are: ', end='')
head.printList()
result = reverseList(head)
print('Nodes of iteratively reversed list are: ', end='')
result.printList()
print()

# Odd length list
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
print('Nodes of original list are: ', end='')
head.printList()
result = reverseList(head)
print('Nodes of recursively reversed list are: ', end='')
result.printList()
print()

