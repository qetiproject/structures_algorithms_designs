# https://leetcode.com/problems/sorting-the-sentence/

# Time complexity: O(N)
# Space complexity: O(N)

# def sortSentence(s: str) -> str:
#     words = s.split()
#     words_dict = {}
#     for word in words:
#         index = int(word[-1])
#         words_dict[index] = word[:-1]

#     result = []
#     for i in range(1, 10):
#         if i in words_dict:
#             result.append(words_dict[i])
#     return " ".join(result)

# Time complexity: O(NlogN)
# Space complexity: O(N)

def sortSentence( s):
    words = s.split()
    sorted_words = words.sort(key=lambda x: x[-1])
    sorted_words_without_indexes = [word[: -1] for word in words]
    return " ".join(sorted_words_without_indexes)

print(sortSentence("is2 sentence4 This1 a3"))

