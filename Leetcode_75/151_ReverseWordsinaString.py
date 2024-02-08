# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

# Time: O(2*N), ქმნის მასივს და მისი ზომა
# Space: O(2*N), საწყისი სტრინგის ზომა
def reverseWords(s: str) -> str:
    s = s.split() # O(N)
    return " ".join(s[::-1]) # O(N) - join, reverse

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))