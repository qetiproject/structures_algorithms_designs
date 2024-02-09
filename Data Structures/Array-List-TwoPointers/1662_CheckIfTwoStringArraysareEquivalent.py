# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

from typing import List

# Time complexity: O(N * M + 1) = O(N * M), სადაც N - word1-ის სიგრძეა, M - word2-ის სიგრძეა, 1 - შედარება
# Space complexity:O(N + M + 1) = O(N + M), სადაც N - word1-ის სიგრძეა, M - word2-ის სიგრძეა, 1 - შედარება
def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    
    word1_str = "".join(word1)
    word2_str = "".join(word2)
    return word1_str == word2_str

print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))