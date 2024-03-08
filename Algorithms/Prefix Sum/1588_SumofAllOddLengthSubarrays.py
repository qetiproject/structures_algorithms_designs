# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

from typing import List

# Time: O(N^2)
# Space: O(1)
# def sumOddLengthSubarrays(arr: List[int]) -> int:
#     result = 0
#     for i in range(len(arr)):
#         for j in range(i, len(arr), 2):
#             result += sum(arr[i:j+1])
#     return result

from typing import List

# time: O(N) # მაგრამ არ მესმის როგორ მუშაობს
def sumOddLengthSubarrays(arr: List[int]) -> int:
    n = len(arr)
    result = 0

    # Iterate through each element in the array
    for i in range(n):
        left_odd = (i + 1) // 2
        right_odd = (n - i) // 2
        left_even = i // 2 + 1
        right_even = (n - i - 1) // 2 + 1

        # Calculate the number of subarrays with each element as the center
        result += arr[i] * (left_odd * right_odd + left_even * right_even)

    return result

print(sumOddLengthSubarrays([1, 4, 2, 5, 3])) 
