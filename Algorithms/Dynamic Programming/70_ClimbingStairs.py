# https://leetcode.com/problems/climbing-stairs/

# იჭრება დროში
def climbStairs(n: int) -> int:
    if n < 3:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)

# Time: O(N)
# Space: O(N)
memo = {1: 1, 2:2}
def climbStairs(n: int) -> int:
    if n not in memo:
        memo[n] = climbStairs(n - 1) + climbStairs(n-2)
    return memo[n]

# tabulation - bottom up
# Time - O(N), ბევრჯერ თუ გამოვიძახებთ მაინც O(N)
memo = [1, 1]
def climbStairs(self, n: int) -> int:
    prev, curr = 1, 1
    for _ in range(len(memo), n + 1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr

# Memorization - top down design
# Time: O(N)
memo = {1:1, 2:2}
def climbStairs(self, n: int) -> int:
    if not n in self.memo:
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    return self.memo[n]
