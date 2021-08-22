"""
LC 268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only 
O(1) extra space complexity and O(n) runtime complexity?

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 
1 is the missing number in the range since it does not appear in nums.
"""

def missingNum(nums):
    # My optimized O(n) solution
    # If the largest number exists, the missing number is wherever the largest number ends up.
    # If the largest number doesn't exist, the result variable is not updated and the largest number is returned.
    idx = 0
    result = len(nums)

    while idx < len(nums):
        if nums[idx] == len(nums):
            # Found last number
            result = idx
            idx += 1
        elif nums[idx] == idx:
            # Advance
            idx += 1
        else:
            # Swap
            tmp = nums[nums[idx]]
            nums[nums[idx]] = nums[idx]
            nums[idx] = tmp
    
    return result


def missingNumSimple(nums):
    # My first simple O(nlogn) solution
    # Sort, then find first index & value mismatch
    nums.sort()

    for i in range(len(nums)):
        if i != nums[i]:
            # Found missing number
            return i
        elif i + 1 == len(nums):
            # Last number is missing
            return i + 1


case1 = [3,0,1]
case2 = [0,1]
case3 = [9,6,4,2,3,5,7,0,1]
case4 = [0]

print(missingNum(case1))
print(missingNum(case2))
print(missingNum(case3))
print(missingNum(case4))

