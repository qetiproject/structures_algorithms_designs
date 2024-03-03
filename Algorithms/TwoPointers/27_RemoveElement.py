# https://leetcode.com/problems/remove-element/

from typing import List

# Time: O(N)
# Space: O(1)
def removeElement(nums: List[int], val: int) -> int:
    k, i = 0, 0

    while i < len(nums):
        if nums[i] != val:
            nums[k] = nums[i]
            k +=1
        i += 1
    return k
