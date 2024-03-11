# https://leetcode.com/problems/find-words-containing-character/

from typing import List

# Time: O(N)
# Space: O(N)
def findWordsContaining(words: List[str], x: str) -> List[int]:
    result = []
    
    for i in range(len(words)):
       if x in words[i]:
           result.append(i)

    return result