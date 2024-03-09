# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from typing import List

# Time: O(N)
# Space: O(N)
def findLucky(arr: List[int]) -> None:
    nums = {}
    result = -1
    for num in arr:
        nums[num] = nums.get(num, 0) + 1
    for num in nums:
        if num == nums[num]:
            result = max(num, result)
    return result

    # x=0
    # f=[]
    # for i in range(len(arr)):
    #     if arr.count(arr[i])==arr[i]:
    #         x+=1
    #         f.append(arr[i])
    # if x==0:
    #     return -1
    # else:
    #     f=sorted(f)
    #     return f[-1]
