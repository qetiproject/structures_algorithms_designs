# https://leetcode.com/problems/number-of-arithmetic-triplets/


from typing import List


def arithmeticTriplets(nums: List[int], diff: int) -> int:
    n = len(nums)
    result = 0

    for i in range(n):
        left = i + 1
        right = n - 1

        while left < right:
            curr_diff = nums[left] - nums[i]

            if curr_diff == diff:
                result += 1
                left += 1
            elif curr_diff > diff:
                right -= 1
            elif curr_diff < diff:
                left += 1

    return result

print(arithmeticTriplets([0,1,4,6,7,10], 2))