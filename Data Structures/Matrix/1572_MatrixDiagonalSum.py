# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List

# Time: O(N)
# Space: O(1)
def diagonalSum(mat: List[List[int]]) -> int:
    result = 0

    for i in range(len(mat)):
        result += mat[i][i]
        result += mat[i][len(mat) - i - 1]

    if len(mat) % 2 == 1:
        result -= mat[len(mat) // 2][len(mat) // 2]

    return result