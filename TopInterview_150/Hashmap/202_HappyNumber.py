# https://leetcode.com/problems/happy-number/

# Time: O(N)
# Space: O(N)
def isHappy(n: int) -> bool:
    result = set()

    while ( n!= 1 and n not in result):
        result.add(n)
        n = sum(int(i) ** 2 for i in str(n))

    return True if n == 1 else False

def isHappy(n: int) -> bool:
    visited = set()  
    while n != 1: 
        sum_of_squares = 0
        while n > 0:
            digit = n % 10
            sum_of_squares += digit ** 2
            n //= 10
        if sum_of_squares in visited:
            return False
        visited.add(sum_of_squares)
        n = sum_of_squares
    
    return True