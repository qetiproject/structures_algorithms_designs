# https://leetcode.com/problems/missing-number/

from typing import List

# Time: O(N ^2)
# Space: O(1)
# def missingNumber(nums: List[int]) -> int:
#     n = len(nums)
#     for i in range(n + 1): # O(N)
#         if i not in nums:# O(N)
#             return i

# Time: O(N)
# Space: O(1)
def missingNumber(nums: List[int]) -> int:
    result = len(nums)
    for i in range(len(nums)): # O(N)
        result += (i - nums[i])
    return result

print(missingNumber([3,0,1]))