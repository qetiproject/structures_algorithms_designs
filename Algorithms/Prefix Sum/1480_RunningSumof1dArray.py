# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List

# Time: O(N)
# Space: O(N)
def runningSum(nums: List[int]) -> List[int]:
    result = [nums[0]]
    for i in range(len(nums)):
        result.append(nums[i] + nums[i - 1])
    return result

# Time: O(N)
# Space: O(1)
def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums

# Time: O(N)
# Space: O(2N)
def runningSum(nums: List[int]) -> List[int]:
    result = nums.copy()
    for i in range(1, len(nums)):
        result[i] +=  result[i - 1]
    return result
