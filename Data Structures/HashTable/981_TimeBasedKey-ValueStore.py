# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    # Time: O(1)
    def __init__(self):
        self.storage = {}

    # Time: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((timestamp, value))

    # Time: O(logN)
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.storage:
            return result
        
        left, right = 0, len(self.storage[key]) - 1

        while left <= right:
            middle = (left + right) // 2
            t, v = self.storage[key][middle]

            if t < timestamp:
                left = middle + 1
                result = v
            elif t > timestamp:
                right = middle - 1
            else:
                return v

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)