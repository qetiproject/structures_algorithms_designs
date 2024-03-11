# https://leetcode.com/problems/rotate-array/

from typing import List

# Time: O(N * K)
# Space: O(1)
def rotate(nums: List[int], k: int) -> None:
    if k > len(nums):
        k %= len(nums)
        
    if k > 0:
        twopt(nums, 0, len(nums) - 1)  
        twopt(nums, 0, k - 1)          
        twopt(nums, k, len(nums) - 1) 
    print(nums)

def twopt(arr, i, j):
    while (i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr