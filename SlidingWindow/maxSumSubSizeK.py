# Fixed window size problem
def max_sub_array_of_size_k(k, arr):
    (start, currSum, maxSum) = (0, 0, 0)

    for end in range(len(arr)):
        # Increase window size by 1
        currSum += arr[end]

        # Check if current window is the max
        if currSum > maxSum:
            maxSum = currSum
        
        # Decrease window size by 1
        if end >= k - 1:
            currSum -= arr[start]
            start += 1

    return maxSum

print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))   # 9
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))      # 7
print(max_sub_array_of_size_k(4, [2, 3, 4, 1, 5]))      # 13
