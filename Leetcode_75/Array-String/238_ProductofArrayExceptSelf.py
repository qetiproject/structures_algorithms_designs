# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

# Time: O(N)
# Space: O(N)
def productExceptSelf(nums: List[int]) -> List[int]:
    answer = [1] * len(nums)

    left, right = 1, 1

    for i in range(len(nums)):
        answer[i] = left
        left *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        answer[i] = answer[i] * right
        right = right * nums[i]

    return answer
