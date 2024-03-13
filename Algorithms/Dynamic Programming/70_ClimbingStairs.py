# https://leetcode.com/problems/climbing-stairs/

# იჭრება დროში
# top down design
# Time: O(2^N)
def climbStairs(n: int) -> int:
    if n < 3:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)

# Memorization - top down design
# Time: O(N)
memo = {1:1, 2:2}
def climbStairs(self, n: int) -> int:
    if not n in self.memo:
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    return self.memo[n]

# bottom up 
# Time: O(N), ბევრჯერ თუ გამოვიძახებთ O(N * M)
def climbStairs(self, n: int) -> int:
    prev, curr = 1, 1
    for _ in range(len(self.memo), n + 1):
        temp = curr
        curr = temp + prev
        prev = temp
    return curr

# tabulation - bottom up
# Time - O(N), ბევრჯერ თუ გამოვიძახებთ მაინც O(N)
def climbStairs(self, n: int) -> int:
    prev, curr = 1, 1
    for _ in range(len(memo), n + 1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr


