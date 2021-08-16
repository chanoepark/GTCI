"""
LC 56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of 
the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def merge(intervals):
    result = []

    # Sort input array
    intervals.sort()

    # Iterate through each interval
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result


case1 = [[1,3],[2,6],[8,10],[15,18]]
case2 = [[1,4],[4,5]]
case3 = [[1,4],[0,4]]
case4 = [[1,4],[2,3]]
case5 = [[1,4],[0,5]]
case6 = [[1,4],[0,0]]
case7 = [[2,3],[4,5],[6,7],[8,9],[1,10]]

print(merge(case1))  # [[1,6],[8,10],[15,18]]
print(merge(case2))  # [[1,5]]
print(merge(case3))  # [[0,4]]
print(merge(case4))  # [[1,4]]
print(merge(case5))  # [[0,5]]
print(merge(case6))  # [[0,0],[1,4]]
print(merge(case7))  # [[1,10]]

