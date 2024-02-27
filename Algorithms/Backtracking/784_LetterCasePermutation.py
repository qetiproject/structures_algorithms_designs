# https://leetcode.com/problems/letter-case-permutation/

from typing import List

# Time: O(N * 2^N)
# Space: O(N * 2^N)
def letterCasePermutation(self, s: str) -> List[str]:
    result = []
    self.letterCasePermutationHelper([], 0, s, result)
    return result

def letterCasePermutationHelper(self, curr: List[str], index: int, s: str, result: List[int]) -> None:
    if index == len(s):
        return result.append("".join(curr))
    
    if s[index].isalpha():
        curr.append(s[index].lower())
        self.letterCasePermutationHelper(curr, index + 1, s, result)
        curr.pop()

        curr.append(s[index].upper())
        self.letterCasePermutationHelper(curr, index + 1, s, result)
        curr.pop()
    else:
        curr.append(s[index])
        self.letterCasePermutationHelper(curr, index + 1, s, result)