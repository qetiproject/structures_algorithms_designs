# https://leetcode.com/problems/combinations/

from typing import List

# Time: O(N * 2^N)
# Space: O(N * 2^N)
def combine(self, n: int, k: int) -> List[List[int]]:
    result = []
    self.combineHelper([], 1, n, k, result)
    return result

# backtracking
def combineHelper(self, current_subset: List[int], curr_number: int,  n: int, k: int, result: List[List[int]]):

    # self.combineHelper(current_subset, curr_number, n, k, result)
    # self.combineHelper(current_subset + [curr_number], curr_number + 1, n, k, result)

    if curr_number > n:
        if len(current_subset) == k:
            result.append(current_subset[:]) # copy()
        return
    
    self.combineHelper(current_subset, curr_number + 1, n, k, result)
    current_subset.append(curr_number)
    self.combineHelper(current_subset, curr_number + 1, n, k, result)
    current_subset.pop()
