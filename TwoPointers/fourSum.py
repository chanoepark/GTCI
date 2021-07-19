"""
LC 18. 4Sum

Given an array nums of n integers, return an array 
of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    1. 0 <= a, b, c, d < n
    2. a, b, c, and d are distinct.
    3. nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

def fourSum(nums, target):
    nums.sort()
        
    quads = []
    
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i - 1]:
            # Skip duplicates
            continue
        for j in range(i + 1, len(nums)-2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                # Skip duplicates
                continue
            
            left = j + 1
            right = len(nums) - 1
            
            while left < right:
                currSum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if currSum == target:
                    quads.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif currSum < target:
                    left += 1
                else:
                    right -= 1
    
    return quads

