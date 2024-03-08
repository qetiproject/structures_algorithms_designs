# https://leetcode.com/problems/left-and-right-sum-differences/

from typing import List

# Time: O(3N)
# Space: O(3N)
def leftRightDifference(nums: List[int]) -> List[int]:
    leftSum = []
    rightSum = [0] * len(nums)
    result = [1] * len(nums)
    k = sum(nums)

    for i in range(len(nums)):
        if i == 0:
            leftSum.append(0)
        else:
            leftSum.append(leftSum[i-1] + nums[i-1])
    
    for i in range(len(nums)):
        if i == len(nums) - 1:
            rightSum.append(0)
        else:
            rightSum[i] = k - leftSum[i] - nums[i]

    for i in range(len(result)):
        result[i] = abs(leftSum[i] - rightSum[i])

    return result


# Time: O(N)
# Space: O(N)
def leftRightDifference(nums: List[int]) -> List[int]:
    n = len(nums)
    left = 0
    right = sum(nums)
    result = []

    for i in range(n):
        right -= nums[i]
        result.append(abs (left - right))
        left += nums[i]
    return result
