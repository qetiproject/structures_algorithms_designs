# https://leetcode.com/problems/3sum/

from typing import List

# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     result = set()
#     n = len(nums)
#     nums.sort()

#     for first_index in range(n):
#         second_index = first_index + 1
#         third_index = n - 1
#         target = -1 * nums[first_index]
#         while second_index < third_index < n:
#             curr_num = nums[second_index] + nums[third_index]
#             if curr_num < target:
#                 second_index += 1
#             elif curr_num > target:
#                 third_index -= 1
#             else:
#                 result.add((nums[first_index], nums[second_index], nums[third_index]))
#                 second_index += 1

#     return list(result)

# Time: O(N^2)
# Space: O(N)

def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)
    nums.sort()

    for first_index in range(n):
        if first_index > 0 and nums[first_index] == nums[first_index - 1]:
            continue
        second_index = first_index + 1
        third_index = n - 1
        target = -1 * nums[first_index]
        while second_index < third_index < n:
            curr_num = nums[second_index] + nums[third_index]
            if curr_num < target:
                second_index += 1
            elif curr_num > target:
                third_index -= 1
            else:
                result.append([nums[first_index], nums[second_index], nums[third_index]])
                second_index += 1

    return result
