# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from typing import Counter, List

# Time: O(N)
# Space: O(1)
def maxOperations(nums: List[int], k: int) -> int:
    res, d = 0, Counter(nums)
    for val1, val1Cnt in d.items():
        val2 = k - val1
        if val1 < val2 or val2 not in d: continue 
        res += min(val1Cnt, d[val2]) if val1 != val2 else val1Cnt//2
    return res

# Time: O(N logN)
# Space: O(1)
def maxOperations(nums: List[int], k: int) -> int:

    nums.sort()
    res, l, r = 0, 0, len(nums) -1 
    while l < r:
        s = nums[l] + nums[r]
        if s > k:
            r -=1
        elif s < k:
            l += 1
        else:
            res += 1
            l += 1
            r -= 1
    return res

# Time: O(N)
# Space: O(N)
def maxOperations(nums: List[int], k: int) -> int:
    result = 0
    found = {}
    for num in nums:
        needed = k - num
        if needed in found and found[needed] > 0:
            result += 1
            found[needed] -= 1
        else: 
            found[num] = found.get(nums, 0) + 1
    return result
