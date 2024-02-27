# https://leetcode.com/problems/permutations/

from typing import List

# Time: O(2 * n! * n + N) # ფოთოლი N!, ზემოთ ხეში იგივე რაოდენობა N!
#Space: O(2 * n! * n) = (n! * n) პერმუტაციის რაოდენობა გამრავლებული nums n რაოდენობა , ხეში მანამდე ზემოთ ფოთლის რაოდენობა ანუ n!
def permute(self, nums: List[int]) -> List[List[int]]:
    result = []
    self.permuteHelper([], nums, result)
    return result

def permuteHelper(self, curr: List[int], nums: List[int], result: List[List[int]]) -> None:
    if len(curr) == len(nums):
        result.append(curr)

    for num in nums:
        if not num in curr:
            self.permuteHelper(curr + [num], nums, result )

# --------------
            
def permuteHelper(self, curr: List[int], nums: List[int], result: List[List[int]]) -> None:
    if len(curr) == len(nums):
        result.append(curr.copy())

    for num in nums:
        if not num in curr:
            curr.append(num)
            self.permuteHelper(curr, nums, result )
            curr.pop()

# --------------
# time: O(2 * N! + N! * N)
# space: O(N * N)
def permute(self, nums: List[int]) -> List[List[int]]:
    result = []
    self.permuteHelper([], set(), nums, result)
    return result


def permuteHelper(self, curr: List[int], nums: List[int], result: List[List[int]]) -> None:
    if len(curr) == len(nums):
        result.append(curr.copy())
        
    for num in nums:
        if not num in curr:
            curr.append(num)
            self.permuteHelper(curr, nums, result )
            curr.pop()

print(permute([1, 2, 3]))