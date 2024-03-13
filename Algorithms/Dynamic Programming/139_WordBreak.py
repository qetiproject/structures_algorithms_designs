# https://leetcode.com/problems/word-break/

from typing import List

# დროში იჭრება
# Time: O(2^N)
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    wordDict = set(wordDict)

    def helper(start_index: int, curr_index: int) -> bool:
        curr_word = s[start_index: curr_index + 1] in wordDict
        if curr_index == len(s) - 1:
            return curr_word
        if curr_word in wordDict:
            using = helper(curr_index + 1, curr_index + 1)
            if using:
                return True
        without_using = helper(start_index, curr_index + 1)
        return without_using
    return helper(0,0)

# Time: O(N^2) 
# Space: O(N^2)
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    memo = {}
    wordDict = set(wordDict)

    def helper(start_index: int, current_index: int) -> bool:
        if (start_index, current_index) in memo:
            return memo[(start_index, current_index)]
        
        current_word = s[start_index: current_index + 1]

        if current_index == len(s) - 1:
            return current_word in wordDict

        if current_word in wordDict:
            using = helper(current_index + 1, current_index + 1)
            if using:
                memo[(start_index, current_index)] = True
                return True
        
        without_using = helper(start_index, current_index + 1)
        memo[(start_index, current_index)] = without_using
        return without_using

    return helper(0, 0)

print(wordBreak("leetcode", ["leet","code"]))