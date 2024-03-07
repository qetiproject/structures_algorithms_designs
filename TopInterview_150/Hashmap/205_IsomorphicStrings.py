# https://leetcode.com/problems/isomorphic-strings/

# Time: O(S + T)
# Space: O(S + T)
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i, j in zip(s, t):
        if (i  in countS and countS[i] != j) or (j in countT and countT[j] != i):
            return False
        countS[i] = j
        countT[j] = i
    return True
