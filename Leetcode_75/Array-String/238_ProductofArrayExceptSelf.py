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

# Time: O(N)
# Space: O(N)
def productExceptSelf(nums: List[int]) -> List[int]:
    prefix_products = [1]
    for i in range(len(nums) - 1):
        prefix_products.append(prefix_products[i] * nums[i])

    suffix_nums = [1] * len(nums)
    for i in range(len(nums) - 1, 0 , -1):
        suffix_nums[i - 1] = suffix_nums[i] * nums[i]
   
    result = []
    for i in range(len(nums)):
        result.append(prefix_products[i] * suffix_nums[i]) 

    return result