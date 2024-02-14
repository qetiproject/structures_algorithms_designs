# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

# Time: O(N + M)
# Space: O(N + M)
def wordPattern(pattern: str, s: str) -> bool:
    word = s.split()
    if len(pattern) != len(word):
        return False
    charToWord = {}
    wordToChar = {}
    for c, w in zip(word, pattern):
        if c in charToWord and charToWord[c] != w:
            return False
        if w in wordToChar and wordToChar[w] != c:
            return False
        charToWord[c] = w
        wordToChar[w] = c
    return True

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))