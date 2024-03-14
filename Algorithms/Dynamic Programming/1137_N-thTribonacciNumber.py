# https://leetcode.com/problems/n-th-tribonacci-number/

# Memorization - top down design
# Time: O(N)
# Space: O(N)
memo = {0:0, 1:1, 2:1}
def tribonacci(n: int) -> int:
    if not n in memo:
        memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    return memo[n]

# tabulation - bottom up
# Time: O(N)
# Space: O(N)
memo = [0, 1, 1]
def tribonacci(self, n: int) -> int:
    for _ in range(len(self.memo), n + 1):
        new_number = self.memo[-1] + self.memo[-2] + self.memo[-3]
        self.memo.append(new_number)
    return self.memo[n]
