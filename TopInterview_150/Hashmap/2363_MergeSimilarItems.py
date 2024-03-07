# https://leetcode.com/problems/merge-similar-items/

from typing import List

# Time: O(N + N * logN)= O(N * logN)
# Space: O(N + N) = O(N)
def mergeSimilarItems(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    result = [] # O(N)
    counts = {} # O(N)

    for pair in items1:
        counts[pair[0]] = pair[1]
    for pair in items2:
        if pair[0] in counts:
            counts[pair[0]] += pair[1]
        else:
            counts[pair[0]] = pair[1]

    for k in sorted(counts):
        result.append([k, counts[k]])
    return result
