# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

# Time: O(N)
# Space: O(1)
def removeDuplicates(nums: List[int]) -> int:
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j

