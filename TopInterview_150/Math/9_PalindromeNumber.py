# https://leetcode.com/problems/palindrome-number/

# Time: O(logN), სადაც N შემავალი რიცხვის 10-ზე გაყოფის რაოდენობაა
# Space: O(1)
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    original_number = x
    reversed_number = 0
    
    while x > 0:
        reversed_number = reversed_number * 10 + x % 10 
        x = x // 10

    return reversed_number == original_number

print(isPalindrome(125))
print(isPalindrome(121))