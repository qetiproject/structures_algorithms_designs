# https://leetcode.com/problems/ransom-note/

# Time: O(M + N), სადაც M - magazine-ის სიგრძეა და N -ransomNote-ის სიგრძე
# Space: O(M), ნებისმისმიერი ზომა - magazine-ის სიგრძე
def canConstruct(ransomNote: str, magazine: str) -> bool:
    countsM = {}

    for m in magazine:
        countsM[m] = countsM.get(m, 0) + 1

    for char in ransomNote:
        if countsM.get(char, 0) == 0:
            return False
        countsM[char] -= 1

    return True