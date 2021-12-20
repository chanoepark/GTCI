"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

Given the weights and profits of 'N' items, we are asked to put these items in 
a knapsack which has a capacity 'C'. The goal is to get the maximum profit 
out of the items in the knapsack. Each item can only be selected once, 
as we don't have multiple quantities of any item.

Let's take the example of Merry, who wants to carry some fruits in the knapsack 
to get maximum profit. Here are the weights and profits of the fruits:
    Items: { Apple, Orange, Banana, Melon }
    Weights: { 2, 3, 1, 4 }
    Profits: { 4, 5, 3, 7 }
    Knapsack capacity: 5

Let's try to put various combinations of fruits in the knapsack, 
such that their total weight is not more than 5:
    Apple + Orange (total weight 5) => 9 profit
    Apple + Banana (total weight 3) => 7 profit
    Orange + Banana (total weight 4) => 8 profit
    Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the 
maximum profit and the total weight does not exceed the capacity.

Problem statement: Given two integer arrays to represent weights and profits of 
'N' items, we need to find a subset of these items which will give us maximum 
profit such that their cumulative weight is not more than a given number 'C'. 
Each item can only be selected once, which means either we put an item in the 
knapsack or we skip it.
"""

# Single array bottom-up dynamic programming solution
# Time: O(n * c)
# Space: O(c)
def solve_knapsack_bottomup_1d(weights, profits, capacity):
    n = len(weights)
    if n == 0 or capacity <= 0 or len(profits) != n:
        return 0
    
    dp = [0 for x in range(capacity + 1)]

    # Populate dp array w/ first weight if it is within capacity
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]
    
    # Process all sub-arrays
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                # Include curr item
                profit1 = profits[i] + dp[c - weights[i]]
            # Exclude curr item
            profit2 = dp[c]
            # Update dp array
            dp[c] = max(profit1, profit2)
    
    return dp[capacity]


# Improved space complexity bottom-up dynamic programming solution
# Time: O(n * c)
# Space: O(c)
def solve_knapsack_bottomup_improved(weights, profits, capacity):
    n = len(weights)
    if n == 0 or capacity <= 0 or len(profits) != n:
        return 0
    
    # Only need one prev row using even/odd trick with mod operator
    dp = [[0 for i in range(capacity + 1)] for j in range(2)]
    
    # Populate dp array w/ first weight if it is within capacity
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0]
        
    # Process all sub-arrays
    for i in range(1, n):
        for c in range(0, capacity + 1):
            profit1, profit2 = 0, 0
            
            if weights[i] <= c:
                # Include curr item
                profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
            # Exclude curr item
            profit2 = dp[(i - 1) % 2][c]
            # Update dp array
            dp[i % 2][c] = max(profit1, profit2)
    
    # Max profit is in bottom right corner
    return dp[(n - 1) % 2][capacity]


# Basic bottom-up dynamic programming solution
# Time & Space: O(n * c) where n is the number of items and c is the capacity
def solve_knapsack_bottomup(weights, profits, capacity):
    n = len(weights)
    if n == 0 or capacity <= 0 or len(profits) != n:
        return 0
    
    dp = [[0 for i in range(capacity + 1)] for j in range(n)]

    # Populate capacity 0 column with 0's since no items can be taken
    for i in range(n):
        dp[i][0] = 0
    
    # Populate item 0 row with profits[i] since only one item can be taken
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
        
    # Process all sub-arrays
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            
            if weights[i] <= c:
                # Include curr item
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # Exclude curr item
            profit2 = dp[i - 1][c]
            # Update dp array
            dp[i][c] = max(profit1, profit2)
    
    # Max profit is in bottom right corner
    return dp[n - 1][capacity]


def solve_knapsack_memoization(weights, profits, capacity):
    dp = [[-1 for i in range(capacity + 1)] for j in range(len(weights))]
    return knapsack_memoization(dp, weights, profits, capacity, 0)


# Top-down dynamic programming solution: memoization
# Time & Space: O(n * c) where n is the number of items and c is the capacity
def knapsack_memoization(dp, weights, profits, capacity, curr_idx):
    if curr_idx >= len(weights) or capacity <= 0:
        return 0

    # Check dp memo to see if curr subproblem is a repeat
    if dp[curr_idx][capacity] != -1:
        return dp[curr_idx][capacity]

    # Profit from including the current item
    profit1 = 0
    if weights[curr_idx] <= capacity:
        new_capacity = capacity - weights[curr_idx]
        profit1 = profits[curr_idx] + knapsack_memoization(dp, 
                                                           weights, 
                                                           profits, 
                                                           new_capacity, 
                                                           curr_idx + 1)

    # Profit from not including the current item
    profit2 = knapsack_recursive(weights, profits, capacity, curr_idx + 1)

    # Update dp memo
    dp[curr_idx][capacity] = max(profit1, profit2)

    return dp[curr_idx][capacity]


def solve_knapsack_recursive(weights, profits, capacity):
    return knapsack_recursive(weights, profits, capacity, 0)


# Recursive solution
# Time: O(2^n) where n is the number of items
# Space: O(n)
def knapsack_recursive(weights, profits, capacity, curr_idx):
    if curr_idx >= len(weights) or capacity <= 0:
        return 0

    # Profit from including the current item
    profit1 = 0
    if weights[curr_idx] <= capacity:
        new_capacity = capacity - weights[curr_idx]
        profit1 = profits[curr_idx] + knapsack_recursive(weights, 
                                                         profits, 
                                                         new_capacity, 
                                                         curr_idx + 1)

    # Profit from not including the current item
    profit2 = knapsack_recursive(weights, profits, capacity, curr_idx + 1)

    return max(profit1, profit2)


profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7
print("Total knapsack profit:", solve_knapsack_bottomup_1d(weights, profits, capacity))
print("Total knapsack profit:", solve_knapsack_bottomup_1d(weights, profits, 6))
print()

print("Total knapsack profit:", solve_knapsack_bottomup_improved(weights, profits, capacity))
print("Total knapsack profit:", solve_knapsack_bottomup_improved(weights, profits, 6))
print()

print("Total knapsack profit:", solve_knapsack_bottomup(weights, profits, capacity))
print("Total knapsack profit:", solve_knapsack_bottomup(weights, profits, 6))
print()

print("Total knapsack profit:", solve_knapsack_memoization(weights, profits, capacity))
print("Total knapsack profit:", solve_knapsack_memoization(weights, profits, 6))
print()

print("Total knapsack profit:", solve_knapsack_recursive(weights, profits, capacity))
print("Total knapsack profit:", solve_knapsack_recursive(weights, profits, 6))
print()

