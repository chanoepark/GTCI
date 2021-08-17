"""
LC 57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
"""

def insert(intervals, newInterval):
    result = []
    i = 0

    # Append intervals that happen before newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    # Append merged interval
    result.append(newInterval)

    # Append remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result


def insertAttempt(intervals, newInterval):
    # My attempted solution, which I gave up on and looked at solution
    # Seems like the better approach was to split up the traversal into multiple parts rather than one big loop
    # Empty list case
    if intervals == []:
        return [newInterval]
    
    result = []
    tmpInterval = []

    # Iterate through each interval
    for i in range(len(intervals)):
        if i == 0 and intervals[i][0] > newInterval[1]:
            intervals.insert(0, newInterval)
            return intervals
        elif i == len(intervals) - 1 and intervals[i][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
        elif intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[1]:
            # Overlap
            if tmpInterval == []:
                tmpInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            else:
                tmpInterval[0] = min(tmpInterval[0], intervals[i][0], newInterval[0])
                tmpInterval[1] = max(tmpInterval[1], intervals[i][1], newInterval[1])
        else:
            # Disjoint
            if tmpInterval != []:
                result.append(tmpInterval)
                tmpInterval = intervals[i].copy()
            else:
                result.append(intervals[i].copy())
                tmpInterval = newInterval.copy()
        # print(f'tmp: {tmpInterval}, curr: {intervals[i]}, result: {result}')
    
    # Insert final interval
    result.append(tmpInterval)
    
    return result


def insertMerge(intervals, newInterval):
    # First solution using mergeIntervals
    result = []

    # Insert newInterval into existing array of intervals
    intervals.append(newInterval)

    # Sort input array
    intervals.sort()

    # Iterate through each interval
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result


print(insert([[1,3],[6,9]], [2,5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(insert([], [5,7]))
print(insert([[1,5]], [2,3]))
print(insert([[1,5]], [2,7]))
print(insert([[1,5]], [6,8]))
print(insert([[1,5]], [0,0]))
print(insert([[2,4],[5,7],[8,10],[11,13]], [3,6]))
print(insert([[3,5],[12,15]], [6,6]))
print(insert([[0,2],[3,3],[6,11]], [9,15]))

