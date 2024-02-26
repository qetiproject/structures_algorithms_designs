# https://leetcode.com/problems/rotting-oranges/

from typing import Deque, List

# Time: O(N * M)
# Space: O(N * M)
def orangesRotting(grid: List[List[int]]) -> int:
    queue = Deque() #გაფუჭებულის კოორდინატები
    fresh_oranges = 0 

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                fresh_oranges += 1
            elif grid[row][col] == 2:
                queue.append((row, col)) 

    if fresh_oranges == 0:
        return 0
    
    minutes_elapsed = -1
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft() 
            neighbours = [( row - 1, col), (row, col + 1), (row + 1, col), (row, col -1)]
            for r, c in neighbours:
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == 1:
                    grid[r][c] == 2 #გავაფუჭოთ მეზობელი
                    queue.append((r, c))
                    fresh_oranges -= 1
        minutes_elapsed += 1 #დავითვალოთ დრო

    return minutes_elapsed if fresh_oranges == 0 else -1

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))


    