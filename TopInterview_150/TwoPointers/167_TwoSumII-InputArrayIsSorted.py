# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

# Time: O(N)
# Space: O(1)
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1

    while i < j:
        curr_target = numbers[i] + numbers[j]
        if curr_target > target:
            j -= 1
        elif curr_target < target:
            i += 1
        else:
            return [ i + 1, j + 1]

