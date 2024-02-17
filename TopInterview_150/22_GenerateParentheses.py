# https://leetcode.com/problems/generate-parentheses/

from typing import List


def generateParenthesis(self, n: int) -> List[str]:
    result = []
    start = 0
    end = 0
    self.generateParenthesisHelper("", start, end, n, result)
    return result

# def generateParenthesisHelper(self, curr: int, start: int, end: int, n: int, result: List[int]) -> None:
#     if len(curr) == 2 * n:
#         result.append(curr)
#         return
#     if start < n:
#         self.generateParenthesisHelper(curr + "(", start + 1, end, n, result)
#     if end < start:
#         self.generateParenthesisHelper(curr + ")", start, end + 1, n, result)

def generateParenthesisHelper(self, curr: int, start: int, end: int, n: int, result: List[int]) -> None:
    if len(curr) == 2 * n:
        result.append("".join(curr))
        return
    if start < n:
        curr.append("(")
        self.generateParenthesisHelper(curr, start + 1, end, n, result)
        curr.pop()
    if end < start:
        curr.append(")")
        self.generateParenthesisHelper(curr, start, end + 1, n, result)
        curr.pop()
