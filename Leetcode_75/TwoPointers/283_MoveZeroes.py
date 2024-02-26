# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# Time: O(N)
# Space: O(1)
def moveZeroes(nums: List[int]) -> None:
    starter = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[starter] = nums[starter], nums[i]
            starter +=1

# def moveZeroes(nums: List[int]):
#     result = []
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             result.append(nums[i])
#         else:
#             count += 1
#     result.extend([0] * count)
#     nums = result
#     return nums

print(moveZeroes([0,1,0,3,12]))