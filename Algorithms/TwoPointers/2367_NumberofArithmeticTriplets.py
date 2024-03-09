# https://leetcode.com/problems/number-of-arithmetic-triplets/


from collections import defaultdict
from typing import List

# Time: O(N ^ 2)
# Space: O(1)
class Solution:
    # def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    #     result = 0
    #     n = len(nums)

    #     for i in range(n - 2):  # O(N)
    #         j = i + 1  
    #         k = j + 1  
    #         while k < n:  # O(N)
    #             diff1 = nums[j] - nums[i]
    #             diff2 = nums[k] - nums[j]

    #             if diff1 == diff2 == diff:
    #                 result += 1
    #                 j += 1  
    #                 k += 1  
    #             elif diff1 < diff2:
    #                 j += 1  
    #             else:
    #                 k += 1 

    #     return result

    # Time: O(N)
    # Space: O(N)
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0
        num_count = {}

        for num in nums:
            if num - diff in num_count and num - 2 * diff in num_count:
                result += num_count[num - diff]
            num_count[num] = num_count.get(num, 0) + 1

        return result

test = Solution()
print(test.arithmeticTriplets([0,1,4,6,7,10], 3))