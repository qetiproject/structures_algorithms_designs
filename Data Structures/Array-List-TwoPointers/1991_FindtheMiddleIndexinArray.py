# https://leetcode.com/problems/find-the-middle-index-in-array/

from typing import List

# Time: O(N)
# Space: O(1)
def findMiddleIndex(self, nums: List[int]) -> int:
    leftSum, rightSum = 0, sum(nums)
    for index, num in enumerate(nums):
        rightSum -= num
        if leftSum == rightSum:
            return index
        leftSum += num
    
    return -1

print(findMiddleIndex([1,7,3,6,5,6]))
# def findMiddleIndex(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         for i in range(0,len(nums)):
#             if sum(nums[:i]) == sum(nums[i+1:]):
#                 return i
#         return -1