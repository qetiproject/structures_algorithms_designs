# https://leetcode.com/problems/greatest-common-divisor-of-strings/

# time: O(N)
# space: O(N)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

sol = Solution()
result = sol.gcdOfStrings("ABCABC", "ABC")
print(result)  # Output: "ABC"