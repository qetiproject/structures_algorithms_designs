# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        curr = self.head
        while index:
            curr = curr.next
            index -= 1
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        self.head, newNode.next = newNode, self.head
        if not self.tail:
            self.tail = self.head
        self.length +=1
        
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head:
            self.tail, self.tail.next = newNode, newNode
        else:
            self.head = self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        elif index == self.length:
            self.addAtTail(val)
        else:
            curr = self.head
            index -= 1
            while index:
                curr = curr.next
                index -= 1
            newNode = Node(val)
            curr.next, newNode.next = newNode, curr.next
            self.length += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            i = index - 1
            while i:
                curr = curr.next
                i -= 1
            curr.next = curr.next.next

        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
    
class Node:
    def __init__(self, value = None, next = None): # ხან გადავცემ ხან არა
        self.value = value  # საწყისი მნიშვნელობა
        self.next = next   # მისამართი რასაც ვამატებთ

class LinkedList():
    # O(1)
    def __init__(self):
        self.head = None
        self.length = 0

    # O(1)
    def size(self):
        return self.length
    
    # O(1) - არ არის დამოკიდებული ელემენტების რაოდენობაზე
    def insert_first(self, value) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    # O(N
    def insert_last(self, value) -> None:
        if self.head is None:
            self.head = Node(value, None)
            self.length += 1
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = Node(value, None)
            self.length += 1

    # O(N) - როცა შუაში ჩამატება გვინდა ელემენტების რაოდენობა იქნება
    def index(self, index, value) -> None:
        if index == 0:
           self.insert_first(value)
        elif index == self.length:
           self.insert_last(value)
        else:
            cur_index = 0
            temp = self.head
            while cur_index < index - 1:
                temp = temp.next
                cur_index += 1
            temp.next = Node(value, temp.next)
            self.length += 1

    # O(N) - თუ ბოლო ელემენტთან მისვლა მოგვიწევს
    def update(self, index, value) -> None:
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp = temp.value

    def remove_first(self) -> None:
        self.head = self.head.next
        self.length -= 1
    
    # O(N)
    def remove_last(self) -> None:
        if self.length == 1:
            self.head = None
            self.length -= 1
        else:
            temp = self.head
            for _ in range(self.length - 1):
                temp = temp.next
            temp.next = None
            self.length -= 1

    # O(N)
    def remove_by_index(self, index) -> None:
        if index == 0:
            self.remove_first()
        else:
            temp = temp.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1

    # O(N)
    def remove_by_value(self, value) -> None:
        temp = self.head
        for index in range(self.length):
            if temp.value == value:
                self.remove_by_index(index)
                return
            temp = temp.next

    # O(N)
    def print_values(self) -> None:
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next