"""
LC 287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem *without modifying* the array nums and uses only *constant extra space*.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1
"""

def findDuplicateNum(nums):
    # Referenced solution
    # Fast & slow pointer approach
    fast = slow = nums[0]

    # Find cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            # Cycle found
            break
    
    # Find start of cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast


def findDuplicateNumBruteforce(nums):
    # O(n^2) bruteforce solution
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return nums[j]


case1 = [1,3,4,2,2]
case2 = [3,1,3,4,2]
case3 = [1,1]
case4 = [1,1,2]

print(findDuplicateNum(case1))
print(findDuplicateNum(case2))
print(findDuplicateNum(case3))
print(findDuplicateNum(case4))

