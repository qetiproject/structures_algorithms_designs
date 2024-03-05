# https://leetcode.com/problems/remove-element/

from typing import List

# Time: O(N)
# Space: O(1)
def removeElement(nums: List[int], val: int) -> int:
    i, j = 0, 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j

print(removeElement([3,2,2,3], 3))