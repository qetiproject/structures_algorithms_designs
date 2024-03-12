class Matrix:
    def __init__(self, rows: int, cols: int):
        self.storage = []
        for _ in range(rows):
            row = cols * [0]
            self.storage.append(row)
        self.sum = 0

    def get_n_rows(self) -> int:
        return len(self.storage)
    
    def get_n_cols(self) -> int:
        return len(self.storage[0])
    
    def get(self, row, col) -> int:
        return self.storage[row][col]
    
    def set(self, row, col, number):
        self.sum += number - self.storage[row][col]
        self.storage[row][col] = number

    def contains(self, number) -> bool:
        for row in range(len(self.storage)):
            if number in self.storage(row):
                return True
        return False
    
    def multiply(self, k):
        rows, cols = len(self.storage), len(self.storage[0])

        for i in range(rows):
            for j in range(cols):
                self.storage[i][j] *= k
        self.sum *=k

    def get_sum(self) -> int:
        return self.sum
    