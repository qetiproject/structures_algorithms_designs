# https://leetcode.com/problems/min-stack/

class MinStack:
    # Time: O(1)
    def __init__(self):
        self.storage = []
        self.mins = []

     # Time: O(1)
    def push(self, val: int) -> None:
        self.storage.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            prev_min = self.mins[-1]
            self.mins.append(min(prev_min, val))
    
    # Time: O(1)
    def pop(self) -> None:
        self.storage.pop()
        self.mins.pop()

    # Time: O(1)
    def top(self) -> int:
        return self.storage[-1]

    # Time: O(1)
    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()