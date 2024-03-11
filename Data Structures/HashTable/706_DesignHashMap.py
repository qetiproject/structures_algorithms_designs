# https://leetcode.com/problems/design-hashmap/


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def _index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._index(key)
        if not self.table[index]:
            self.table[index] = ListNode(key, value)
            return
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next

    def get(self, key: int) -> int:
        index = self._index(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return -1
    
    def remove(self, key: int) -> None:
        index = self._index(key)
        current = self.table[index]
        if not current:
            return
        if current.key == key:
            self.table[index] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next - current.next.next
                return
            current = current.next

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)
            


class HashList:
    def __init__(self):
        self.buckets = [] 
        for i in range(5):
            self.buckets.append([])
        self.length = 0
        
    # O(1)
    def get_length(self) -> int:
        return self.length

    def append(self, string: str) -> None:
        index = self._get_bucket_index(string)
        self.buckets[index] = string
        self.length += 1

    # O(1)
    def contains(self, string: str) -> bool:
        index = self._get_bucket_index(string)
        return string in self.buckets[index]
    
    # O(1)
    def remove(self, string: str) -> None:
        if not self.contains(string):
            return
        index = self._get_bucket_index(string)
        self.buckets[index].remove(string)
        self.length -= 1

    def _get_bucket_index(self, string: str) -> int: 
        index = hash(string) % len(self.buckets)
        return index

# დაწერეთ test_hash_list ფუნქცია, რომელიც გატესტავს თქვენს HashList კლასს. ეცადეთ, დაფაროთ ყველა შემთხვევა.
"Your code goes here"
def test_hash_list():
    hash_list = HashList()
    assert hash_list.get_length() == 0

    hash_list.append("abc")
    assert hash_list.get_length() == 1
    assert hash_list.contains("abc") == True

    hash_list.append("abc")
    hash_list.append("cvs")
    assert hash_list.get_length() == 3
    
    hash_list.remove("abc")
    assert hash_list.get_length() == 2

    print("All test cases passed!")

# test_hash_list()