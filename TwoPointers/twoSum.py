"""
LC 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    # My solution
    (start, end) = (0, len(nums) - 1)
    original = {}
    idx = 0
    
    # Create dict containing original indices
    for num in nums:
        if num in original:
            original[num].append(idx)
        else:
            original[num] = [idx]
        idx += 1
    
    # Sort array of integers
    nums.sort()
    
    # Loop while pointers don't cross
    while start < end:
        x = nums[start]
        y = nums[end]
        
        # Increment left if current sum is smaller
        if x + y < target:
            start += 1
            
        # Decrement right if current sum is larger
        elif x + y > target:
            end -= 1
        
        # Solution found
        else:
            if len(original[x]) != 1:
                return [original[x][0], original[x][1]]
            return [original[x][0], original[y][0]]


def twoSumBruteForce(nums, target):
    # My brute force solution
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSumComplement(nums, target):
    # Better solution from LC discussion post
    map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in map:
            return (map[complement], i)
        map[nums[i]] = i


case1 = [2,7,11,15]
target1 = 9

case2 = [3,2,4]
target2 = 6

case3 = [3,3]
target3 = 6

print(twoSum(case1, target1)) # [0,1]
print(twoSum(case2, target2)) # [1,2]
print(twoSum(case3, target3)) # [0,1]

