# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# time: O(N)
# space: O(N)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        
        for candy in candies:
            if (candy + extraCandies) >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result