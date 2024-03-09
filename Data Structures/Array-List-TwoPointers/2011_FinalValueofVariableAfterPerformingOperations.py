# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import List

# Time: O(N)
# Space: O(1)
def finalValueAfterOperations(operations: List[str]) -> int:
    result = 0

    for op in operations:
        if op == "++X" or op == "X++":
            result += 1
        else:
            result -= 1 
    return result