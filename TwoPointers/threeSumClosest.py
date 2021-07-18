"""
LC 16. 3Sum Closest

Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
"""

# Similar to 3sum; O(n^2)
# Referenced solution
def threeSumClosest(nums, target):
    nums.sort()
    dist = float('inf')

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            
            # Update closest distance
            if abs(target - currSum) < abs(dist):
                dist = target - currSum
            
            # Adjust pointer
            if currSum < target:
                left += 1
            else:
                right -= 1
        
        if dist == 0:
            # Found exact match
            break
    
    return target - dist

