# https://leetcode.com/problems/sort-colors/

from typing import List

# Time: O(N ^ 2)
# Space: O(1)
# def sortColors(self, nums: List[int]) -> None:
#     n = len(nums)

#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] > nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]

# Time: O(N)
# Space: O(1)
def sortColors(self, nums: List[int]) -> None:
    zero_index = 0
    two_index = len(nums) - 1
    curr_index = 0

    while curr_index <= two_index:
        if nums[curr_index] == 0:
            nums[curr_index], nums[zero_index] = nums[zero_index], nums[curr_index]
            curr_index += 1
            zero_index += 1
        elif nums[curr_index] == 1:
            curr_index += 1
        elif nums[curr_index] == 2:
            nums[curr_index], nums[two_index] = nums[two_index], nums[curr_index]
            two_index -= 1

