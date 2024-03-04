# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

from typing import List

# Time: O(2N)
# Space: O(1)
def isPrefixString(s: str, words: List[str]) -> bool:
    for i in range(1, len(words) + 1):
        if s == ''.join(words[:i]):
            return True
    return False

# print(isPrefixString("iloveleetcode", ["i","love","leetcode", "apples"]))
print(isPrefixString("a", ["aa","aaaa","banana"]))