# https://leetcode.com/problems/divisor-game/

# Time: O(N)
# Space: O(N)
def divisorGame(n: int) -> bool:
    result = [False] * (n + 1)
    result[0] = True
    result[1] = False

    for s in range(2, n+ 1):
        for j in range(1, s):
            if result[s-j] == False and s % j == 0:
                result[s] = True
    return result[n]
