# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from typing import Deque, List

# როცა უმოკლესი გზა გვინდა BFS ვიყენებთ უმრავლეს შემთხვევაში
def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    queue = Deque()
    queue.append((entrance[0], entrance[1], 0)) # row, col, distance - რამდენი ნაბიჯითაა დაშორებული საწყისიდან
    while queue:
        row, col, distance = queue.popleft()

        # თუ გადავიჩეხეთ ან კედელზე ვართ, ვერაფერს ვიზამთ ამ წერტილიდან
        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[row]) or maze[row][col] == "+":
                continue

        # თუ გასასვლელთან ვართ და ეს წერტილი დაშორებულია საწყისი წერტილიდან
        if (row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[row]) - 1) and distance > 0:
            return distance
        
        # საწყისი წერტილი კედლად გადავაკეთოთ და გავიდეთ მეზობლებთან
        maze[row][col] = "+"

        queue.append((row - 1, col, distance + 1)) # top
        queue.append((row, col + 1, distance + 1)) #right
        queue.append((row + 1, col, distance + 1)) # bottom
        queue.append((row, col - 1, distance + 1)) # left

    return -1


print(nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0]))