from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    answer = [1] * len(nums)

    left, right = 1, 1

    for i in range(len(nums)):
        answer[i] = left
        left *= nums[i]

    for i in range(len(nums)-1, -1, -1):
        print(nums[i])
        answer[i] = answer[i] * right
        right = right * nums[i]

    return answer

print(productExceptSelf([1,2,3,4]))