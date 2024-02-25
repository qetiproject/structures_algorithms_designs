# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

# Time: O(N)
# Space: O(1)
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    result = len(nums) + 1
    left = 0
    curr_sum = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        if curr_sum >= target:
            while curr_sum >= target:
                result = min(result, right - left + 1)
                curr_sum -= nums[left]
                left += 1

    if result == len(nums) + 1:
        return 0
    
    return result