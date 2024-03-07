# https://leetcode.com/problems/find-pivot-index/

from typing import List

# Time: O(N)
# Space: O(1)
def pivotIndex(nums: List[int]) -> int:
    leftSum, rightSum = 0, sum(nums)
    for idx, ele in enumerate(nums):
        rightSum -= ele
        if leftSum == rightSum:
            return idx      
        leftSum += ele
    return -1       

# Time: O(3N)
# Space: O(2N)
def pivotIndex(nums: List[int]) -> int:
    prefix_sum = nums.copy()

    for i in range(1, len(nums)):
        prefix_sum[i] += prefix_sum[i - 1]

    suffix_sum = nums.copy()
    for i in range(len(nums) - 2, -1, -1):
        suffix_sum[i] += suffix_sum[i + 1]

    for i in range(len(nums)):
        if prefix_sum[i] == suffix_sum[i]:
            return i 
        
    return -1