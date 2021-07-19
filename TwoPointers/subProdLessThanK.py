"""
LC 713. Subarray Product Less Than K

Given an array of integers nums and an integer k, 
return the number of contiguous subarrays 
where the product of all the elements in the subarray is strictly less than k.
"""

def numSubarrayProductLessThanKImproved(nums, k):
    # O(n) solution referenced from solution
    left = 0
    prod = 1
    result = 0
    
    for right in range(len(nums)):
        prod *= nums[right]
        
        while prod >= k and left <= right:
            prod /= nums[left]
            left += 1
        
        result += right - left + 1
    
    return result


def numSubarrayProductLessThanK(nums, k):
    # My bruteforce O(n^2) solution
    result = 0
        
    for left in range(len(nums)):
        right = left
        curr = 1
        
        while right < len(nums):
            curr *= nums[right]
            
            if curr < k:
                # Valid subarray
                result += 1
                right += 1
            else:
                # Invalid subarray
                break
    
    return result

