# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# Time: O(N)
# Space: O(1)
def largestAltitude(gain: List[int]) -> int:
    result = 0
    path = 0
    for i in range(len(gain)):
        path += gain[i]
        if path > result:
            result = path
    return result

print(largestAltitude([-5,1,5,0,-7]))