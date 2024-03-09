# https://leetcode.com/problems/missing-number/

from typing import List

# Time: O(N ^2)
# Space: O(1)
def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n + 1): # O(N)
        if i not in nums:# O(N)
            return i

# Time: O(N)
# Space: O(1)
def missingNumber(nums: List[int]) -> int:
    result = len(nums)
    for i in range(len(nums)): # O(N)
        result += (i - nums[i])
    return result

# Time: O(N)
# Space: O(N)
def missingNumber(nums: List[int]) -> int:
    result = set(nums)
    for i in range(len(nums) + 1):
        if i not in result:
            return i

# Time: O(N)
# Space: O(1)
def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2  
    actual_sum = sum(nums)  
    return expected_sum - actual_sum