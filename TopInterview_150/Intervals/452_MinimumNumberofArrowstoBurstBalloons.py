# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List

# Time: O(N*logN)
# Space: O(N)
def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort(lambda interval: interval[1])
    result, end = 0, points[0][1]

    for i in range(1, len(points)):
        if end < points[i][0]:
            result += 1
            end = points[i][1]

    return result