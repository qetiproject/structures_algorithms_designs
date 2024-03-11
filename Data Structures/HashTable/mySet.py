class MySet:
    def __init__(self):
        self.buckets = [[], [], [], []]
        self.length = 0

    # O(1)
    def get_length(self) -> int:
        return self.length

    # O(1)
    def contains(self, number: int) -> bool:
        index = self._get_bucket_index(number)
        return number in self.buckets[index]
    
    # O(1)
    def add(self, number: int) -> None:
        if self.contains(number):
          return
        index = self._get_bucket_index(index)
        self.buckets[index].append(number)
        self.length += 1

    # O(1)
    def remove(self, number: int) ->None:
        if not self.contains(number):
            return
        index = self._get_bucket_index(number)
        self.buckets[index].remove(number)
        self.length -= 1

    # O(1)    
    def _get_bucket_index(self, number: int) -> int: # _ შიდა ფუნქცია
        index = hash(number) % len(self.buckets)
        return index
    

def test_my_set():
    my_set = MySet()
    assert my_set.get_length() == 0
    assert my_set.contains(1) == False

    my_set.add(1)
    assert my_set.get_length() == 1
    assert my_set.contains(1) == True

    my_set.add(2)
    assert my_set.get_length() == 2
    assert my_set.contains(1) == True
    assert my_set.contains(2) == True

    my_set.remove(2)
    assert my_set.get_length() == 1
    assert my_set.contains(1) == True
    assert my_set.contains(2) == False

    print("All test cases passed!")

test_my_set()