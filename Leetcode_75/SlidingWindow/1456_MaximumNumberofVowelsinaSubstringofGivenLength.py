# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Time: O(len(S))
# Space: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        count = 0
        vowels = ["a", "e", "i", "o", "u"]

        for i in range(min(len(s), k)):
            if s[i] in vowels:
                count += 1
        result = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1

            result = max(result, count)
        return result
