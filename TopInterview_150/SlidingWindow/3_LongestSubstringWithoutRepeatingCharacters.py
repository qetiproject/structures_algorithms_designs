# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time: O(2*N)= O(N)
# Space: O(1)
def lengthOfLongestSubstring(self, s: str) -> int:
    result = 0
    left = 0
    charSet = set()

    for right in range(len(s)):
        if s[right] not in charSet:
            charSet.add(s[right])
            result = max(result, right - left + 1)
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
        

    return result