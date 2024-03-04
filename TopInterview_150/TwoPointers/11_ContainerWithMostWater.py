# https://leetcode.com/problems/container-with-most-water/

from typing import List

# Time: O(N)
# Space: O(1)
def maxArea(height: List[int]) -> int:
    result = 0
    left  = 0
    right = len(height) - 1

    while left < right:
        left_height = height[left]
        right_height = height[right]
        area = min(left_height, right_height) * (right - left)
        result = max(result, area)

        if left_height < right_height:
            left += 1
        elif left_height > right_height:
            right -= 1
        else:
            left += 1
            right -= 1

    return result
