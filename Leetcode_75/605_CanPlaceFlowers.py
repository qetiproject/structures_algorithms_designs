# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# time: O(N)
# space: O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and ( i == 0 or flowerbed[i-1] == 0) and ( i ==len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False