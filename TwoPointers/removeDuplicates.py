"""
LC 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.
"""

def removeDuplicates(nums):
    prev = 1
    
    for curr in range(1, len(nums)):
        if nums[curr] != nums[prev - 1]:
            nums[prev] = nums[curr]
            prev += 1
    
    return prev


case1 = [1,1,2]
expectedCase1 = [1,2]
case2 = [0,0,1,1,1,2,2,3,3,4]
expectedCase2 = [0,1,2,3,4]

result1 = removeDuplicates(case1)
result2 = removeDuplicates(case2)

assert result1 == len(expectedCase1)
assert result2 == len(expectedCase2)

for i in range(result1):
    assert case1[i] == expectedCase1[i]

for i in range(result2):
    assert case2[i] == expectedCase2[i]

