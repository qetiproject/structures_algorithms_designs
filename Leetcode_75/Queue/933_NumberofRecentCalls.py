# https://leetcode.com/problems/number-of-recent-calls/

from typing import Deque


class RecentCounter:

    # Space: O(N)
    def __init__(self):
        self.storage = Deque()
        
    # Time: O(N)
    # Space: O(1)
    def ping(self, t: int) -> int:
        self.storage.append(t)
        while self.storage[0] < t - 3000:
            self.storage.popleft()
        return len(self.storage)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)