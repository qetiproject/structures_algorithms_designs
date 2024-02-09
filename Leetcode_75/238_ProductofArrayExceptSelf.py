# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# Time: O(N)
# Space: O(N)
def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * len(nums)

    suffix = prefix  = 1
    for  i in range(1, len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    for  i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result

# print(productExceptSelf([1,2,3,4]))

# Time: O(N)
# Space: O(1), we are using contant extra space
def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * len(nums)
    for  i in range(1, len(nums)):
        result[i] = nums[i - 1] * result[i - 1]
        
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * suffix
        suffix = suffix * nums[i]

    return result

print(productExceptSelf([1,2,3,4]))

# არ ვიცი space რამდენად სწორია, მგონი O(1)-ია ორივეში