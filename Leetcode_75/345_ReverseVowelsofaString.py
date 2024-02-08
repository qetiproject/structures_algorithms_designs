# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75


def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s = list(s)
    p1, p2 = 0, len(s) - 1
    while p1 < p2:
        while p1 < p2 and s[p1] not in vowels:
            p1 += 1
        while p1 < p2  and s[p2] not in vowels:
            p2 -= 1
        s[p1], s[p2] = s[p2], s[p1]
        p1 += 1
        p2 -= 1

    return "".join(s)


s = "hello"
#"holle"
print(reverseVowels(s))