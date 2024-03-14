# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List

# Time: O(N^2)
# Space: O(N)
def getRow(rowIndex: int) -> List[int]:
    result = [1]

    for _ in range(rowIndex):
        next_row = [0] * (len(result) + 1)
        for j in range(len(result)):
            next_row[j] += result[j]
            next_row[j + 1] += result[j]
        result = next_row        
    return result
