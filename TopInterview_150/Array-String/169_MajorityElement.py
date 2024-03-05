# https://leetcode.com/problems/majority-element/

from typing import List

# Time: O(N)
# Space: O(1)
def majorityElement(nums: List[int]) -> int:
    majority_number = nums[0]
    majority_count = 1

    for i in range(1, len(nums)):
        if nums[i] == majority_number:
            majority_count += 1
        else:
            majority_count -= 1
        
        if majority_count == -1:
            majority_number = nums[i]
            majority_count = 1
    
    return majority_number

# Time: O(N)
# Space: O(N)
def majorityElement(nums: List[int]) -> int:
    majority_dict = {}
    result = 0
    count = 1
    for num in nums:
        if not num in majority_dict:
            majority_dict[num] = 1
            if result == 0:
                result = num
        else:
            majority_dict[num] += 1
            if  majority_dict[num] > count:
                count = majority_dict[num]
                result = num
            
    return result