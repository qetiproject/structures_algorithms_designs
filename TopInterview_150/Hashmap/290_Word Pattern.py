# https://leetcode.com/problems/word-pattern/

# Time: O(N + M)
# Space: O(N + M)
def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    charToWord = {}
    wordToChar = {}
    for c, w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w:
            return False
        if w in wordToChar and wordToChar[w] != c:
            return False
        charToWord[c] = w
        wordToChar[w] = c
        
    return True

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))