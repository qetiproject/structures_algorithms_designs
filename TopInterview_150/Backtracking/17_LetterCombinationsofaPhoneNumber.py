# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

def letterCombinations(self, digits: str) -> List[str]:
    result = []
    if not digits:
        return result
    self.letterCombinationsHelper("", digits, 0, result)
    self.letterCombinationsHelper([], digits, 0, result)
    return result

def letterCombinationsHelper(self, curr: str, digits: str, index: int, result: List[int]) -> None:
    if index == len(digits):
        result.append(curr)
        return
    
    for ch in letters[digits[index]]:
        self.letterCombinationsHelper(curr + [ch], digits, index + 1, result)

# --------------
# time: O(4^N + 4^N /2 *N) = O(4^N * N), მარცხენა მხარე ნაკლებია, /2 კი იკვეცება. where N is len(digits)
# space: O(4^N + 4^N /2 *N) = O(4^N * N)
def letterCombinationsHelper(self, curr: str, digits: str, index: int, result: List[int]) -> None:
    if index == len(digits):
        result.append("".join(curr)) # N - კოპირება/join()
        return
    
    for ch in letters[digits[index]]:
        curr.append(ch)
        self.letterCombinationsHelper(curr, digits, index + 1, result)
        curr.pop()
