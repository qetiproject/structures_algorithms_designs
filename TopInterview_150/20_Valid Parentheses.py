# https://leetcode.com/problems/valid-parentheses/

# Time: O(N)
# Space: O(1)
# def isValid(s: str) -> bool:
#     counter = 0
#     for ch in s:
#         if ch == "(":
#             counter += 1
#         elif ch == ")":
#             if counter == 0:
#                 return False
#             else:
#                 counter -= 1
#     if counter > 0:
#         return False
#     return True

# Time: O(N)
# Space: O(N)
# def isValid(s: str) -> bool:
#     stack = []
#     for ch in s:
#         if ch == "(":
#             stack.append(ch)
#         elif ch == ")":
#             if not stack:
#                 return False
#             else:
#                 stack.pop()
#     if stack:
#         return False
#     return True

# Time: O(N)
# Space: O(N)
def isValid(s: str) -> bool:
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []

    for ch in s:
        if ch in brackets:
            stack.append(ch)
        else:
            if not stack:
                return False
            if brackets[stack[-1]] == ch:
                stack.pop()
            else:
                return False
            
    return len(stack) == 0

print(isValid("()[]{}"))
print(isValid("(]"))