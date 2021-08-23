"""
LC 442. Find All Duplicates in an Array

Given an integer array nums of length n where 
all the integers of nums are in the range [1, n] and 
each integer appears once or twice, 
return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
"""

def findAllDuplicateNums(nums):
    idx = 0
    duplicateNums = []

    # Sort
    while idx < len(nums):
        target = nums[idx] - 1
        if nums[idx] != nums[target]:
            # Swap
            nums[idx], nums[target] = nums[target], nums[idx]
        else:
            # Advance
            idx += 1
    
    # Find index & value mismatch
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            duplicateNums.append(nums[i])
    
    return duplicateNums


case1 = [4,3,2,7,8,2,3,1]
case2 = [1,1,2]
case3 = [1]

print(findAllDuplicateNums(case1))
print(findAllDuplicateNums(case2))
print(findAllDuplicateNums(case3))

