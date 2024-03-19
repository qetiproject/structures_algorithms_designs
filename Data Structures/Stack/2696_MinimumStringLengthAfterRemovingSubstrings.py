# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

# Time: O(N)
# Space: O(N)
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if stack  and stack[-1] + char in ("AB", "CD"):
                stack.pop()
            else:
                stack.append(char)

        return len(stack)


class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            if "AB" in s:
                s = s.replace("AB","")
            elif "CD" in s:
                s = s.replace("CD","")
        return len(s)
    
def minLength(self, s: str) -> int:
    sb = list(s)
    i = 0
    while i < len(sb) - 1:
        if sb[i] == 'A' and sb[i+1] == 'B':
            del sb[i:i+2]
            i = max(0, i-1)
        elif sb[i] == 'C' and sb[i+1] == 'D':
            del sb[i:i+2]
            i = max(0, i-1)
        else:
            i += 1
    return len(sb)