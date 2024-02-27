# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = list(word)
        left = 0

        for i in range(len(word)):
            if result[i] == ch:
                while left < i:
                    result[i], result[left] = result[left], result[i]
                    left += 1
                    i -= 1
                return "".join(result)

        return word
