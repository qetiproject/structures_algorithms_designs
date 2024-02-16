# https://leetcode.com/problems/baseball-game/

from typing import List

# Time: O(N)
# Space: O(N)
def calPoints(operations: List[str]) -> int:
    stack = []

    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))

    return sum(stack)

print(calPoints(["5","2","C","D","+"]))