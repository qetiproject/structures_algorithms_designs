# https://leetcode.com/problems/two-sum/

from typing import List

# Time: O(N ^ 2)
# Space: O(N), თუ ყველა ელემენტის შენახვა მოგვიწევს
def twoSum(nums: List[int], target: int) -> List[int]:
    
    for x_index, x in enumerate(nums):
        for y_index, y in enumerate(nums):
            if x_index != y_index and x + y == target:
                return [x_index, y_index]
 
# Time: O(N)
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for index, num in enumerate(nums):
        wanted = target - num
        if wanted in seen:
            return [seen[wanted], index]
        else:
            seen[num] = index

print(twoSum([2,7,11,15], 9))