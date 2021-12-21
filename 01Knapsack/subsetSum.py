"""
https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

Given a set of positive numbers, determine if a subset exists whose sum is 
equal to a given number 'S'.

Example 1:
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}

Example 2:
Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}

Example 3:
Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.
"""
# My bottom-up DP solution w/ 1D dp array
# Time: O(n * s) where n is the length of input nums and s is target_sum
# Space: O(s)
def solve_isSubsetSum_1D(nums, target_sum):
    if target_sum < 0:
        return False
    
    dp = [False] * (target_sum + 1)  # Init DP array
    dp[0] = True  # Populate col 0

    # Process sub-arrays
    for curr in nums:
        # Need to process from right-to-left
        for s in range(target_sum, curr - 1, -1):
            dp[s] = dp[s] or dp[s - curr]
    
    return dp[target_sum]


# My bottom-up DP solution w/ 2 row dp array
# Time: O(n * s) where n is the length of input nums and s is target_sum
# Space: O(s)
def solve_isSubsetSum_2r(nums, target_sum):
    if target_sum < 0:
        return False
    
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(2)]

    # Populate col 0
    for i in range(2):
        dp[i][0] = True
    
    # Populate row 0
    for s in range(target_sum + 1):
        dp[0][s] = nums[0] == s
    
    # Process sub-arrays
    for i in range(1, n):
        for s in range(1, target_sum + 1):
            idx = (i - 1) % 2
            # Check excluding curr element
            if dp[idx][s]:
                dp[i % 2][s] = dp[idx][s]
            # Check including curr element
            elif nums[i] <= s:
                dp[i % 2][s] = dp[idx][s - nums[i]]
    
    return dp[(n - 1) % 2][s]


# My basic bottom-up DP solution
# Time: O(n * s) where n is the length of input nums and s is target_sum
# Space: O(n * s)
def solve_isSubsetSum_dp(nums, target_sum):
    if target_sum < 0:
        return False
    
    n = len(nums)
    dp = [[False] * (target_sum + 1) for _ in range(n)]

    # Populate col 0
    for i in range(n):
        dp[i][0] = True
    
    # Populate row 0
    for s in range(target_sum + 1):
        dp[0][s] = nums[0] == s
    
    # Process sub-arrays
    for i in range(1, n):
        for s in range(1, target_sum + 1):
            # Check excluding curr element
            if dp[i - 1][s]:
                dp[i][s] = dp[i - 1][s]
            # Check including curr element
            elif nums[i] <= s:
                dp[i][s] = dp[i - 1][s - nums[i]]
    
    return dp[n - 1][s]


# My memoization solution
# Time: O(n * s) where n is the length of input nums and s is target_sum
# Space: O(n * s)
def solve_isSubsetSum_memo(nums, target_sum):
    memo = [[None] * (target_sum + 1) for _ in range(len(nums))]
    return isSubsetSum_memo(memo, nums, target_sum, 0)


def isSubsetSum_memo(memo, nums, target_sum, curr_idx):
    # Base cases
    if curr_idx >= len(nums) or target_sum < 0:
        return False
    
    if target_sum == 0:
        return True
    
    # Check memo
    if memo[curr_idx][target_sum] is not None:
        return memo[curr_idx][target_sum]
    
    # Compute result
    result = isSubsetSum_memo(memo, nums, target_sum, curr_idx + 1) or \
             isSubsetSum_memo(memo, nums, target_sum - nums[curr_idx], curr_idx + 1)
    memo[curr_idx][target_sum] = result  # Update memo

    return result


# My recursive solution
# Time: O(2 ^ n) where n is the length of input nums
# Space: O(n) recursion stack
def solve_isSubsetSum_recursive(nums, target_sum):
    return isSubsetSum_recursive(nums, target_sum, 0)


def isSubsetSum_recursive(nums, target_sum, curr_idx):
    # Base cases
    if curr_idx >= len(nums) or target_sum < 0:
        return False
    
    if target_sum == 0:
        return True
    
    # Recursion: Either include or don't include curr element
    return isSubsetSum_recursive(nums, target_sum, curr_idx + 1) or \
           isSubsetSum_recursive(nums, target_sum - nums[curr_idx], curr_idx + 1)


# True, True, False
test_cases = [([1,2,3,7], 6), ([1,2,7,1,5], 10), ([1,3,4,8], 6)]

print('Bottom-Up DP w/ 1D DP array')
for (test_case, target_sum) in test_cases:
    print(solve_isSubsetSum_1D(test_case, target_sum))
print()

print('Bottom-Up DP w/ 2 row DP array')
for (test_case, target_sum) in test_cases:
    print(solve_isSubsetSum_2r(test_case, target_sum))
print()

print('Basic Bottom-Up DP')
for (test_case, target_sum) in test_cases:
    print(solve_isSubsetSum_dp(test_case, target_sum))
print()

print('Memoization')
for (test_case, target_sum) in test_cases:
    print(solve_isSubsetSum_memo(test_case, target_sum))
print()

print('Recursive')
for (test_case, target_sum) in test_cases:
    print(solve_isSubsetSum_recursive(test_case, target_sum))

