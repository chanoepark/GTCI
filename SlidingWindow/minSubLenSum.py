# Dynamic window size problem
def smallest_subarray_with_given_sum(s, arr):
    (start, currSum, currLen, minLen) = (0, 0, 0, float('inf'))

    for end in range(len(arr)):
        # Increase window by 1
        currSum += arr[end]
        currLen += 1
        
        # Check if requirement has been met
        while currSum >= s:
            # Check if current window is the min
            if currLen < minLen:
                minLen = currLen
            
            # Decrease window by 1
            currSum -= arr[start]
            currLen -= 1
            start += 1

    return minLen if minLen != float('inf') else 0

print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))  # 2
print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))     # 1
print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))     # 3
print(smallest_subarray_with_given_sum(10, [1, 1, 1, 1]))       # 0
