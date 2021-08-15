"""
LC 234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def compareLists(head, head2):
    if not head or not head2:
        return True
    elif head.val != head2.val:
        return False
    return compareLists(head.next, head2.next)


def isPalindrome(head):
    # Find center node
    center = middleNode(head)

    # Reverse second half of list
    head2 = reverse(center)

    # Compare the two halves
    return compareLists(head, head2)


def isPalindromeImproved(head):
    rev = None
    slow = fast = head

    # Reverse first half of list while finding center node
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    
    if fast:
        # Advance slow one step forward from center
        slow = slow.next
    
    # Compare the two halves
    while rev and rev.val == slow.val:
        rev = rev.next
        slow = slow.next

    return not rev


# Odd length palindrome
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)
print(f'Is palindrome: {isPalindrome(head)}')

# Even length non-palindrome
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(2)
print(f'Is palindrome: {isPalindrome(head)}')

# Even length palindrome
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(6)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(2)
print(f'Is palindrome: {isPalindrome(head)}')

# Odd length non-palindrome
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(6)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(2)
print(f'Is palindrome: {isPalindrome(head)}')

