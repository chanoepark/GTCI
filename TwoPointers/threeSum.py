"""
LC 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# Two pointer approach where you look for a complement pair to the current value
# i.e. X + Y + Z = 0 -> Y + Z = -X, so looking for Y + Z which complements X
# O(n^2): Helper function is O(n) and helper function is invoked n times
# Had the idea but struggled to implement; consulted solution
def searchPair(nums, target, left, triplets):
    right = len(nums) - 1
    
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            # Found triplet
            triplets.append([-target, nums[left], nums[right]])
            
            # Adjust pointers
            left += 1
            right -= 1
            
            # Skip duplicates on both sides
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
            
        elif curr < target:
            # Adjust left pointer
            left += 1
        else:
            # Adjust right pointer
            right -= 1
    

def threeSum(nums):
    nums.sort()

    triplets = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            # Skip over duplicates
            continue
        searchPair(nums, -nums[i], i + 1, triplets)
    
    return triplets


case1 = [-1,0,1,2,-1,-4]
case2 = []
case3 = [0]

print(threeSum(case1)) # [[-1,-1,2],[-1,0,1]]
print(threeSum(case2)) # []
print(threeSum(case3)) # []

