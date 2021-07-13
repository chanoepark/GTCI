"""
LC 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
"""

# Two pointers approach w/ pointers starting at each end of the array and moving inwards
# O(n)
def sortedSquaresOutInPointers(nums):
    # Based on LC discussion post; same idea as my original solution, but reverse direction and simpler code
    left = 0
    right = len(nums) - 1
    result = []
    
    while left <= right:
        leftSq = nums[left] ** 2
        rightSq = nums[right] ** 2
        
        if leftSq > rightSq:
            result.insert(0, leftSq)
            left += 1
        else:
            result.insert(0, rightSq)
            right -= 1
    
    return result


# Two pointers approach w/ pointers starting within the array and moving outwards
# O(n)
def sortedSquaresInOutPointers(nums):
    # My solution
    left = 0
    result = []

    while left + 1 < len(nums) and nums[left + 1] < 0:
        # Set left pointer to last negative number
        left += 1
    
    right = left + 1
    
    if left == 0 and nums[left] >= 0:
        # All positive numbers
        for i in range(len(nums)):
            nums[i] *= nums[i]
        return nums
    elif right == len(nums):
        # All negative numbers
        for i in reversed(range(len(nums))):
            result.append(nums[i] ** 2)
        return result
    
    while left >= 0 and right < len(nums):
        # Mix of both positive & negative numbers
        leftSq = nums[left] ** 2
        rightSq = nums[right] ** 2
        
        if leftSq < rightSq:
            result.append(leftSq)
            left -= 1
        else:
            result.append(rightSq)
            right += 1
        
    if left < 0:
        # Complete right
        while right < len(nums):
            result.append(nums[right] ** 2)
            right += 1
    else:
        # Complete left
        while left >= 0:
            result.append(nums[left] ** 2)
            left -= 1
    
    return result


# Trivial solution using sort
# O(nlogn)
def sortedSquaresSimple(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]
    
    nums.sort()
    
    return nums


case1 = [0, 1, 2, 3, 4]
case2 = [-5, -4, -3, -2, -1]
case3 = [-2, 0]
case4 = [-1, 2, 2]
case5 = [-4,-1,0,3,10]

print(sortedSquaresInOutPointers(case1)) # [0, 1, 4, 9, 16]
print(sortedSquaresInOutPointers(case2)) # [1, 4, 9, 16, 25]
print(sortedSquaresInOutPointers(case3)) # [0, 4]
print(sortedSquaresInOutPointers(case4)) # [1, 4, 4]
print(sortedSquaresInOutPointers(case5)) # [0, 1, 9, 16, 100]

