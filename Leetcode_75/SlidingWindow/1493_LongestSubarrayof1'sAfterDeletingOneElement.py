# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import List

# Time: O(2* N) = O(N)
# Space: O(1)
def longestSubarray(self, nums: List[int]) -> int:
    result = 0
    left = 0
    zeroes = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1
        if zeroes > 1:
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
        result = max(result, right - left + 1 - 1)

    return result