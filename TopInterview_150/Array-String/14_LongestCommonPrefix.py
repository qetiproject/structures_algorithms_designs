# https://leetcode.com/problems/longest-common-prefix/

from typing import List

# Time: O(N * M), N - length of v, M - max length in v word
# Space: O(1)
def longestCommonPrefix(v: List[str]) -> str:
    result = v[0]
    
    for i in v:
        while not i.startswith(result):
            result = result[:-1]
            if not result:
                return ""
    return result

# Time: O(N * logN)
# Space: O(min(len(first), len(last)))
def longestCommonPrefix( v: List[str]) -> str:

    result = ""
    v = sorted(v)
    first, last = v[0], v[-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return result
        result += first[i]
    return result
