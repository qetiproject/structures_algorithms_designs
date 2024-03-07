# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

# Time: O(N * logN)
# Space: O(N)
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda interval: interval[1])
    result, end = 0, intervals[0][1]

    for interval in intervals[1:]:
        if end > interval[0]:
            result += 1
        else:
            end = interval[1]
    return result