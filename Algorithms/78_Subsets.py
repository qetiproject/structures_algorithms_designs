# https://leetcode.com/problems/subsets/

from typing import List

# Time: O(2^N + (2^N *N)) = O(2^N * N(N + 1))= O(N * 2^N)

# შემოვლა: 2^N + (2^N - 1) = 2*2^N -1 = 2^N; # 2^N  - ფოთლების რაოდენობა, 2^N -1 - ფოთლებამდე node-ების რაოდენობა
# კოპირება: 2^N * N , სადაც 2^N ფოთლების რაოდენობა, N  ცალი კოპირება

# Space: O(N * (2^N/ 2)) = O(N * 2^N)
def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []
    # self.subsets_helper([], nums, 0, result)
    self.subsetsHelperBacktracking([], nums, 0, result)
    return result

def subsets_helper(self, current_subset: List[int], nums: List[int], index: int, result: List[List[int]]) -> None:
    if index == len(nums):
        result.append(current_subset)
        return

    self.subsets_helper(current_subset, nums, index + 1, result)
    self.subsets_helper(current_subset + [nums[index]], nums, index + 1, result)

# Time: O(N * 2^N)
# Space: O(N * (2^N/ 2)) = O(N * 2^N)
# backtracking
def subsetsHelperBacktracking(self, current_subset: List[int], nums: List[int], index: int, result: List[List[int]]) -> None:
    if index == len(nums):
        result.append(current_subset.copy())
        return

    self.subsets_helper(current_subset, nums, index + 1, result)
    current_subset.append(nums[index])
    self.subsets_helper(current_subset, nums, index + 1, result)
    current_subset.pop()

