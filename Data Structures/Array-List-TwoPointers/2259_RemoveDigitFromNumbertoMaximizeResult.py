# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

# Time; O(N * M)
# Space: O(N)
def removeDigit(number: str, digit: str) -> str:
    result = ""

    i = 0
    while i < len(number):
        prev = result
        if number[i] == digit:
            result = number[0:i] + number[i+1:len(number)]
        if prev > result:
            result = prev
        i += 1
        
    return result

print(removeDigit("1231", "1"))