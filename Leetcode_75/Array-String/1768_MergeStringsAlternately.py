# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

# Time: O(max(len1, len2) )
# Space: O(1)?
def mergeAlternately(word1: str, word2: str) -> str:
    len1, len2 = len(word1), len(word2)
    max_len = max(len1, len2)
    
    result = ""

    for i in range(max_len):
        if i < len1:
            result+= word1[i]
        if i < len2:
            result += word2[i]
        
    return result

# print(mergeAlternately("abc", "pqrs"), "result")

# Time: O(max(len(word1), len(word2)))
# Space: O(N)
def mergeAlternately(word1: str, word2: str) -> str:
    i, j = 0, 0
    result = []

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    
    result.append(word1[i:])
    result.append(word2[j:])

    return "".join(result)

print(mergeAlternately("abc", "pqrs"))