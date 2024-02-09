# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# Time: O(N)
# Space: O(1)
def increasingTriplet(nums: List[int]) -> bool:
    # float("inf") - უმცირესი რიცხვის საპოვნელად გამოიყენება ან მიმდევრობების
    min1 = min2 = float("inf")
    for n in nums:
        if min1 < min2 < n:
           return True
        elif n < min1:
            min1 = n
        elif min1 < n < min2:
            min2 = n
    return False

print(increasingTriplet([20,100,10,12,5,13]))