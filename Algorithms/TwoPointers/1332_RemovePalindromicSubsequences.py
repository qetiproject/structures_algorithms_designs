# https://leetcode.com/problems/remove-palindromic-subsequences/

# Time: O(N)
# Space: O(1)
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[:len(s)][::-1]:
            return 1
        else:
            return 2

test = Solution()
print(test.removePalindromeSub("ababbba"))