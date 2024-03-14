# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

from typing import List

# Time: O(N)
# Space: O(N)
def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    result = [words[0]]

    for i in range(1,len(groups)):
        if groups[i] != groups[i - 1]:
            result.append(words[i])
    return result

# Time: O(N)
# Space: O(N)
def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    return [words[i] for i, x in enumerate(groups) if i == 0 or x != groups[i - 1]]

print(getLongestSubsequence(["a","b","c","d"], [1,0,1,1]))