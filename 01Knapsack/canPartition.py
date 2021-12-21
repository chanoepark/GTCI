"""
LC 416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of 
elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
# Bottom-up DP solution w/ 1D array
# Time: O(n * s) where n is the input length and s is the target sum
# Space: O(s)
def solve_can_partition_dp_1D(nums):
    input_sum = sum(nums)

    if input_sum % 2:
        return False

    target_sum = input_sum // 2

    dp = [False] * (target_sum + 1)  # Init dp array
    dp[0] = True  # Populate 1st col w/ True for base case

    # Process sub-arrays
    for curr in nums:
        for s in range(target_sum, curr - 1, -1):
            dp[s] = dp[s] or dp[s - curr]
    
    return dp[target_sum]


# Bottom-up DP solution w/ 2 row dp array
# Time: O(n * s) where n is the input length and s is the target sum
# Space: O(s)
def solve_can_partition_dp_2r(nums):
    input_sum = sum(nums)

    if input_sum % 2:
        return False
    
    target_sum = input_sum // 2
    n = len(nums)
    dp = [[False for s in range(target_sum + 1)] for i in range(2)]

    # Populate target_sum 0 column with True since it's always achievable
    for i in range(2):
        dp[i][0] = True
    
    # Populate curr_idx 0 row target_sum nums[0] column with True
    # With only one element, it can only satisfy target_sum equal to itself
    for s in range(1, target_sum + 1):
        if nums[0] == s:
            dp[0][s] = True
    
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

    return dp[(n - 1) % 2][target_sum]


# Bottom-up DP solution w/ n row dp array
# Time: O(n * s) where n is the input length and s is the target sum
# Space: O(n * s)
def solve_can_partition_dp(nums):
    input_sum = sum(nums)

    if input_sum % 2:
        return False
    
    target_sum = input_sum // 2
    n = len(nums)
    dp = [[False for s in range(target_sum + 1)] for i in range(n)]

    # Populate target_sum 0 column with True since it's always achievable
    for i in range(n):
        dp[i][0] = True
    
    # Populate curr_idx 0 row target_sum nums[0] column with True
    # With only one element, it can only satisfy target_sum equal to itself
    for s in range(1, target_sum + 1):
        if nums[0] == s:
            dp[0][s] = True
    
    # Process sub-arrays
    for i in range(1, n):
        for s in range(1, target_sum + 1):
            # Check excluding curr element
            if dp[i - 1][s]:
                dp[i][s] = dp[i - 1][s]
            # Check including curr element
            elif nums[i] <= s:
                dp[i][s] = dp[i - 1][s - nums[i]]

    return dp[n - 1][target_sum]


# Memoization solution
# Time: O(n * s) where n is the input length and s is the target sum
# Space: O(n * s)
def solve_can_partition_memo(nums):
    input_sum = sum(nums)

    if input_sum % 2:
        return False
    
    target_sum = input_sum // 2
    memo = [[None for i in range(target_sum + 1)] for j in range(len(nums))]

    return can_partition_memo(memo, nums, target_sum, 0)


def can_partition_memo(memo, nums, target_sum, curr_idx):
    if target_sum == 0:
        # Success base case
        return True
    
    if curr_idx >= len(nums) or target_sum < 0:
        # Failure case
        return False
    
    # Check memo
    if memo[curr_idx][target_sum] is not None:
        return memo[curr_idx][target_sum]
    
    # Recursion: Either include or don't include the current element
    result = can_partition_memo(memo, nums, target_sum - nums[curr_idx], curr_idx + 1) or \
             can_partition_memo(memo, nums, target_sum, curr_idx + 1)
    memo[curr_idx][target_sum] = result  # Update memo

    return result


# Brute force solution
# Time: O(2^n)
# Space: O(n)
def solve_can_partition_recursive(nums):
    input_sum = sum(nums)

    if input_sum % 2:
        return False

    return can_partition_recursive(nums, input_sum // 2, 0)


def can_partition_recursive(nums, target_sum, curr_idx):
    if target_sum == 0:
        # Success base case
        return True
    
    if curr_idx >= len(nums) or target_sum < 0:
        # Failure case
        return False
    
    # Recursion: Either include or don't include the current element
    return can_partition_recursive(nums, target_sum - nums[curr_idx], curr_idx + 1) or \
           can_partition_recursive(nums, target_sum, curr_idx + 1)


# True, False, True, True, False, False
test_cases = [[1,5,11,5], [1,2,3,5], [1,2,3,4], [1,1,3,4,7], [2,3,4,6], [1,2,5]]

print('Bottom-up DP 1D array')
for test_case in test_cases:
    print(solve_can_partition_dp_1D(test_case))
print()

print('Bottom-up DP 2 row array')
for test_case in test_cases:
    print(solve_can_partition_dp_2r(test_case))
print()

print('Bottom-up DP')
for test_case in test_cases:
    print(solve_can_partition_dp(test_case))
print()

print('Memoization')
for test_case in test_cases:
    print(solve_can_partition_memo(test_case))
print()

print('Recursive')
for test_case in test_cases:
    print(solve_can_partition_recursive(test_case))

