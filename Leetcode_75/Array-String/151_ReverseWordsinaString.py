# https://leetcode.com/problems/reverse-words-in-a-string
# Time: O(2*N), ქმნის მასივს და მისი ზომა
# Space: O(2*N), საწყისი სტრინგის ზომა
# def reverseWords(s: str) -> str:
#     s = s.split() # O(N)
#     return " ".join(s[::-1]) # O(N) - join, reverse

# Time: O(N)
# Space: O(1)
class Solution:
    def reverseWords(self,  s: str) -> str:
        result = ""
        n = len(s)
        i, j = 0, 0

        while j < n:
            while i < n and s[i] == " ":
                i += 1
            if i >= n:
                break
            j = i + 1
            while j < n and s[j] != " ":
                j += 1
            sub = s[i:j]
            if result == "":
                result = sub
            else:
                result = sub + " " + result
            i = j+ 1
        return result