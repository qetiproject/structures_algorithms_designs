# https://leetcode.com/problems/length-of-last-word/

# Time: O(N)
# Space: O(N)
def lengthOfLastWord(s: str) -> int:
    s = s.split()
    return len(s[-1])