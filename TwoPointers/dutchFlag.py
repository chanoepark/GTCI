"""
Dutch National Flag Problem

Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers 
that is why it is called Dutch National Flag problem.

Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]

Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2]
"""

def dutchFlagSort(flag):
    left = curr = 0
    right = len(flag) - 1

    while curr <= right:
        if flag[curr] == 0:
            flag[curr], flag[left] = flag[left], flag[curr]
            left += 1
        elif flag[curr] == 2:
            flag[curr], flag[right] = flag[right], flag[curr]
            right -= 1
            curr -= 1
        curr += 1
    
    return flag


case1 = [1, 0, 2, 1, 0]
case2 = [2, 2, 0, 1, 2, 0]

print(dutchFlagSort(case1))
print(dutchFlagSort(case2))

