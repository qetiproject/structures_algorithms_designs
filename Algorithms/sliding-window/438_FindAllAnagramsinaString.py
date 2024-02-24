# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List

def index(self, ch: str) -> int:
    return ord(ch) - ord("a")

# Time: O(S + P)
# Space: O(S)
def findAnagrams(self, s: str, p: str) -> List[int]:
    result = []
    s_counts = 26 * [0]
    p_counts = 26 * [0]
    k = len(p)

    for ch in s:
        s_counts[self.index(ch)] += 1

    for i in range(k):
        p_counts[self.index(s[i])] += 1
        if i >= k:
            ch = s[i - k]
            p_counts[self.index(ch)] -= 1
        if i>= k - 1:
            is_anagram = s_counts == p_counts
            if is_anagram:
                result.append(i - k + 1)

    return result