# https://leetcode.com/problems/removing-stars-from-a-string/

# Time: O(N)
# Space: O(N)
def removeStars(self, s: str) -> str:
    stack = []

    for ch in s:
        if ch != "*":
            stack.append(ch)
        else:
            stack.pop()

    return "".join(stack)

