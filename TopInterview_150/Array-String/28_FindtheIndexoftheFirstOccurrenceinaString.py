# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Time: O((N -M + 1) * M) = O(N * M)
# Space: O(1)
def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i: i+m] == needle:
            return i
    return -1