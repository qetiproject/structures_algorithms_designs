# https://leetcode.com/problems/asteroid-collision/

from typing import List

# Time: O(N)
# Space: O(1)
def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    n = len(asteroids)
    j = 0

    for i in range(n):
        asteroid = asteroids[i]

        while j > 0 and asteroids[j-1] > 0 and asteroid < 0 and asteroids[j - 1] < abs(asteroid):
            j -= 1
        
        if j == 0 or asteroid > 0 or asteroids[j - 1] < 0:
            asteroids[j] = asteroid
            j +=1
        elif asteroids[j-1] == abs(asteroid):
            j -= 1
        
    return asteroids[:j]