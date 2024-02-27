# https://leetcode.com/problems/combination-sum/

from typing import List

# Time: O(N * 2^N)
# Space: O(N * 2^N)
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []
    self.combinationSumHelper([], 0, target, candidates, 0, result)
    return result

def combinationSumHelper(self, current_subset, current_sum, target, candidates, index, result) -> None:
    # if index == len(candidates):
    #     if current_sum == target:
    #         result.append(current_subset)
    #     return
    # self.combinationSumHelper(current_subset, current_sum, target, candidates, index + 1, result)
    # self.combinationSumHelper(current_subset + [candidates[index]], current_sum + candidates[index], target, candidates, index, result)

    if current_sum == target:
        result.append(current_subset.copy())
    if index == len(candidates) or current_sum > target:
        return
    
    self.combinationSumHelper(current_subset, current_sum, target, candidates, index + 1, result)
    current_subset.append(candidates[index])
    self.combinationSumHelper(current_subset, current_sum + candidates[index], target, candidates, index, result)
    current_subset.pop()