# https://leetcode.com/problems/summary-ranges/

from typing import List

# Time: O(N)
# Space: O(N)
def summaryRanges(nums: List[int]) -> List[str]:
    result = []

    if not nums:
        return []
    
    start = nums[0]
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i + 1] - nums[i] > 1:
            if nums[i] == start:
                result.append(f"{start}")
            else:
                result.append(f"{start}->{nums[i]}")
            start = nums[(i + 1) % len(nums)]

    return result

def summaryRanges(nums: List[int]) -> List[str]:
    if not nums: return []
    intervals = [[nums[0], nums[0]]]
    for i in nums[1:]:
        if intervals[-1][-1] + 1 != i:
            intervals.append([i, i])
        else:
            intervals[-1][-1] = i
    return [str(start) if start == end else f"{start}->{end}" for start, end in intervals]