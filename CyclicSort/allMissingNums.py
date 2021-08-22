"""
LC 448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
"""

def allMissingNumsInPlace(nums):
    # O(n) solution referenced from LC discussion post
    # Mark the value that curr index points to as negative
    # Filter the list for indices with positive values
    for i in range(len(nums)):
        targetIdx = abs(nums[i]) - 1
        nums[targetIdx] = -abs(nums[targetIdx])
    return [i + 1 for i, num in enumerate(nums) if num > 0]


def allMissingNums(nums):
    # O(n) solution
    result = []
    idx = 0

    # Sort
    while idx < len(nums):
        targetIdx = nums[idx] - 1
        if nums[idx] != nums[targetIdx]:
            # Swap
            nums[idx], nums[targetIdx] = nums[targetIdx], nums[idx]
        else:
            # Advance
            idx += 1
    
    # Find index & value mismatch
    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(i + 1)

    return result


case1 = [4,3,2,7,8,2,3,1]
case2 = [1,1]

print(allMissingNumsInPlace(case1))
print(allMissingNumsInPlace(case2))

