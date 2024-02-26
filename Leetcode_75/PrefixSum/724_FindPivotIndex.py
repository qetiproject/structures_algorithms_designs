# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# Time: O(N)
# Space: O(1)
def pivotIndex(nums: List[int]) -> int:
    leftSum, rightSum = 0, sum(nums)
    for idx, ele in enumerate(nums):
        rightSum -= ele
        if leftSum == rightSum:
            return idx      
        leftSum += ele
    return -1       
       
print(pivotIndex([1,7,3,6,5,6]))