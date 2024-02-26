# https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List

# Time: O(N)
# Space: O(1)
def longestOnes(self, nums: List[int], k: int) -> int:
    result = 0
    start, end, count_zero = 0, 0, 0
    while end < len(nums):
        if nums[end] == 0:
            count_zero += 1
        while count_zero > k:
            if nums[start] == 0:
                count_zero -= 1
            start += 1
        
        result = max(result, end - start + 1)
        end += 1
    return result