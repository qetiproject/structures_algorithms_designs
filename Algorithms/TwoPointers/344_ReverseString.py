# https://leetcode.com/problems/reverse-string/

from typing import List

# Time: O(N)
# Space: O(1)
def reverseString(self, s: List[str]) -> None:
    i, j = 0, len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
