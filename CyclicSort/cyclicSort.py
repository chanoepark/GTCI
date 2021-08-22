"""
GTCI Cyclic Sort

We are given an array containing ‘n’ objects. 
Each object, when created, was assigned a unique number from 
1 to ‘n’ based on their creation sequence. 
This means that the object with sequence number ‘3’ 
was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number 
in O(n) and without any extra space. 
For simplicity, let’s assume we are passed an integer array 
containing only the sequence numbers, though each number is actually an object.

Example 1:
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]

Example 2:
Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]

Example 3:
Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""

def cyclicSort(nums):
    idx = 0

    while idx < len(nums):
        if idx + 1 == nums[idx]:
            # Advance
            idx += 1
        else:
            # Swap
            tmp = nums[nums[idx] - 1]
            nums[nums[idx] - 1] = nums[idx]
            nums[idx] = tmp
    
    return nums


case1 = [3, 1, 5, 4, 2]
case2 = [2, 6, 4, 3, 1, 5]
case3 = [1, 5, 6, 4, 3, 2]

print(cyclicSort(case1))
print(cyclicSort(case2))
print(cyclicSort(case3))

