# https://leetcode.com/problems/fibonacci-number/

# top down
# O(2^N)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# bottom up 
# Time: O(N), ბევრჯერ თუ გამოვიძახებთ O(N * M)
def fib(n: int) -> int:
    first = 0
    second = 1
    for _ in range(n):
        third = first + second
        first = second
        second = third
    return first

# Memorization - top down design
# Time: O(N)
memo = {}
def fib(n: int) -> int:
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

memo = {0: 0, 1:1}
def fib(n: int) -> int:
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

# tabulation - bottom up
# Time - O(N), ბევრჯერ თუ გამოვიძახებთ მაინც O(N)
memo = [0, 1]
def fib(n: int) -> int:
    for  _ in range(len(memo),n - 1):
        new_number = memo[-1] + memo[-2]
        memo.append(new_number)
    return memo[n]