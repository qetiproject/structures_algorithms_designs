# https://leetcode.com/problems/design-hashset/

from collections import defaultdict

class MyHashSet:

    def __init__(self):
        self.storage=defaultdict(int)        

    def add(self, key: int) -> None:
        self.storage[key] = True

    def remove(self, key: int) -> None:
        self.storage[key] = False

    def contains(self, key: int) -> bool:
        return self.storage[key]


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
obj.remove(1)
param_3 = obj.contains(2)
