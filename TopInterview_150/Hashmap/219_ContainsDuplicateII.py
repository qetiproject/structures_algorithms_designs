# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List

# Time:O(N)
# Space: O(N)
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    result = {}

    for index, num in enumerate(nums):
        if num in result and abs(index - result[num] <= k):
            return True
        result[num] = index  

    return False