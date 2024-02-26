# https://leetcode.com/problems/maximum-average-subarray-i/

from typing import List

# Time: O(N)
# Space: O(1)
# k =3, nums[1, 2] + nums[3], -nums[0] ვამატებთ მომდევნო ინდექსის რიცხვს მარჯვნივ, მაკლებს წინა ინდექსს დასაწყისიდან 
def findMaxAverage(self, nums: List[int], k: int) -> float:
    result = float("-inf") # უმცირესი რიცხვი

    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if i >= k:
            curr_sum -= nums[i - k]
        if i >= k -1:
            result = max(result, curr_sum / k)
    return result