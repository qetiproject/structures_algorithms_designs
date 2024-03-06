# https://leetcode.com/problems/roman-to-integer/

# Time: O(N)
# Space: O(1) რადგან ვიცით კონკრეტულად რას შეიცავს
def romanToInt(s: str) -> int:
    data_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i  < len(s) - 1 and data_dict[s[i]] < data_dict[s[i + 1]]:
            result -= data_dict[s[i]]
        else:
            result += data_dict[i]
    
    return result