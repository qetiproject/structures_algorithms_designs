# https://leetcode.com/problems/implement-stack-using-queues/

from typing import Deque


class MyStack:
    def __init__(self):
        self.storage = []

    def push(self, x: int) -> None:
        self.storage.append(x)

    def pop(self) -> int:
        return self.storage.pop()

    def top(self) -> int:
        return self.storage[-1]

    def empty(self) -> bool:
        return len(self.storage) == 0
    

class MyStackUsinQueue:
    def __init__(self):
        self.storage = Deque()

    def push(self, x: int) -> None:
        self.storage.append(x)

    def pop(self) -> int:
        for i in range(len(self.storage) - 1):
            self.push(self.storage.popleft())
        return self.storage.popleft()

    def top(self) -> int:
        return self.storage[-1]

    def empty(self) -> bool:
        return len(self.storage) == 0