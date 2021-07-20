"""
LC 142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that 
can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def getCycleLen(slow):
    curr = slow
    cycleLen = 0
    
    while True:
        curr = curr.next
        cycleLen += 1
        if curr == slow:
            break
    
    return cycleLen


def detectCycle(head):
    slow, fast = head, head

    # Find length of LinkedList cycle
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        # Cycle exists
        if slow == fast:
            # Find cycle length
            cycleLen = getCycleLen(slow)

            # Find start of cycle
            slow, fast = head, head

            # Move fast pointer cycleLen ahead of slow pointer
            for _ in range(cycleLen):
                fast = fast.next
            
            # Start of cycle is found when the two pointers meet
            while slow != fast:
                fast = fast.next
                slow = slow.next

            return slow
    
    # Cycle doesn't exist
    return None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = head.next.next
print('LinkedList cycle starts at:', detectCycle(head).val)

head.next.next.next.next.next = head.next.next.next
print('LinkedList cycle starts at:', detectCycle(head).val)

head.next.next.next.next.next = head
print('LinkedList cycle starts at:', detectCycle(head).val)

