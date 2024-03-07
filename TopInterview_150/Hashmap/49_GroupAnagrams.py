# https://leetcode.com/problems/group-anagrams/

from typing import List

# Time: O(N * K*logK)
# Space: O(N)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = []
    strsDict = {}

    for s in strs:
        sorted_str = "".join(sorted(s))
        if sorted_str in strsDict:
            result[strsDict[sorted_str]].append(s)
        else:
            strsDict[sorted_str] = len(result)
            result.append([s])
    return result