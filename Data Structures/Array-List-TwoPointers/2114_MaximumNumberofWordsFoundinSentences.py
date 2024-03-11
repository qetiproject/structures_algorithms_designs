# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

from typing import List

# Time: O(N)
# Space: O(N)
def mostWordsFound(sentences: List[str]) -> int:
    result = 0
    for s in sentences:
        k = s.split()
        if len(k) > result:
            result = len(k)
    return result

# Time: O(N * M)
# Space: O(N)
def mostWordsFound(sentences: List[str]) -> int:
    result = []

    for i in sentences:
        count = 0
        for j in i:
            if j == " ":
                count += 1
        count += 1
        result.append(count)
    return max(result)