# https://leetcode.com/problems/counting-bits/

from typing import List

# Time; O(N)
# Space: O(N)
def countBits(n: int) -> List[int]:
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i // 2] + (i % 2)
    return result