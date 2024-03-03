# https://leetcode.com/problems/reverse-only-letters/

# Time: O(N)
# Space: O(N), რადგან მხოლოდ ლათინური ასოებია ჩათვლილი O(1)
def reverseOnlyLetters(s: str) -> str:
    i, j = 0, len(s) - 1
    s = list(s)
    while i < j:
        if s[i].isalpha() and s[j].isalpha():
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
            
    return "".join(s)

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))