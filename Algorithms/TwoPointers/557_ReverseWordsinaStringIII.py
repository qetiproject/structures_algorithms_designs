# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Time: O(N + K * M)
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        start = 0
        for end in range(len(s)): # O(K) - len(s)
            if s[end] == " ":
                result += s[start:end][::-1] + " " # O(M) - len(w) reversed
                start = end + 1

        result +=s[start:][::-1] # O(N)

        return result