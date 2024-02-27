# https://leetcode.com/problems/generate-parentheses/

from typing import List

# Time complexity: O( 2N * 2^ 2*N)= O(N * 2^N) 2^N - ხეში ნოუდების რაოდენობა, ყველა პერმუტაციის რაოდენობა, 2N - კოპირების ოპერაცია
# Space complexity: O( 2N * 2^ 2*N)= O(N * 2^N)
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
    # if not (end <= start <= n):
    #     return # ამას თუ დავწერთ ქვემოთა 2 if არ დაგვჭირდება, შიდა ტანი ისედაც იმუშავებს

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
