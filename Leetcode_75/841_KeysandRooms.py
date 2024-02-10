# https://leetcode.com/problems/keys-and-rooms/

from typing import List

# time: O(N), N is nums of keys
# time: O(R), where R is number of rooms
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    stack = [0] # პირველი ოთახის გასაღები, რომელიც გვაქვს
    visited = set() # რომელ ოთახშიც ნამყოფი ვართ

    while stack:
        key = stack.pop() # გასაღების აღება
        room = rooms[key] # ოთახში შესვლა
        visited.add(key)
        for key in room:
            if  key not in visited:
                stack.append(key)

    return len(visited) == len(rooms)

print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

        
