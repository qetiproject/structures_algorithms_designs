class ListQueue:
    # O(1)
    def __init__(self) -> None:
        self.storage = []
        self.current = 0

    # O(1)
    def size(self) -> int:
        # return len(self.storage)
        return len(self.storage) - self.current

    # O(1) @
    def enqueue(self, value: any) -> None: # ჩამატება
        self.storage.append(value)

    # O(1) @
    def dequeue(self) -> any: #წაშლა
        # return self.storage.pop(0) # O(N) - გადაყოლა უწევს ბოლოდან 
        if self.current > 100: 
            self.storage = self.storage[self.current: ]# O(N)
            self.current = 0
        self.current += 1
        return self.storage[self.current - 1]

    # O(1)
    def front(self) -> any: # 1 ელ
        # return self.storage[0]
        return self.storage[self.current]

    # O(1)
    def rear(self) -> any: # ბოლო ელ
        return self.storage[-1]