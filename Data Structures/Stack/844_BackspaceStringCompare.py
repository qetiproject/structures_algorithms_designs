# https://leetcode.com/problems/backspace-string-compare/

# Time: O(N)
# Space: O(N)
# def backspaceCompare(s: str, t: str) -> bool:
#     return apply_backspace(s) == apply_backspace(t)

# def apply_backspace(string: str) -> str:
#     stack = []

#     for char in string:
#         if char != "#":
#             stack.append(char)
#         elif stack:
#             stack.pop()
#     return stack

# print(backspaceCompare("ab#c", "ad#c"))


def backspaceCompare(S: str, T: str) -> bool:
    i, j = len(S), len(T) # two indexes, start outside of string to make loop simpler
    
    while i >= 0 and j >= 0:
        back = 1 # backspace counter, move back at least one character
        while back > 0:
            i -= 1
            back += 1 if i >= 0 and S[i] == '#' else -1 # if hashtag found increase backspace counter, otherwise decrease it

        back = 1
        while back > 0:
            j -= 1
            back += 1 if j >= 0 and T[j] == '#' else -1
        
        if i >= 0 and j >= 0 and S[i] != T[j]: # done with backspaces, compare current character
            return False
    
    return i < 0 and j < 0 # return True if both indexes passed both strings fully