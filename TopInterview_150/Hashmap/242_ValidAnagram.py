# https://leetcode.com/problems/valid-anagram/

from typing import Counter

# Time complexity: O(N)
# Space complexity: O(1)
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Time complexity: O(S + T)
# Space complexity: O(S + T)
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    for i in countS:
        if countS[i] != countT.get(i, 0):
            return False
        # if countS[i] != 0:
            # return False
        
    return True

