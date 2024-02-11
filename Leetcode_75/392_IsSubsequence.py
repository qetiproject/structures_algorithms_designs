# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

# Time: O(N)
# Space: O(1)
def isSubsequence(s: str, t: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

print(isSubsequence("abc", "ahbgdc"))