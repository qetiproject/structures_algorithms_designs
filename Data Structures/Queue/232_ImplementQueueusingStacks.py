class Node:
    def __init__(self, value = None, next = None):
        self.value =value
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.head = Node()
        self.length = 0

    def size(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.length == 0
    
    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is emty!")
        
        last_elem = self.top()
        self.head = self.head.next
        self.length -= 1

        return last_elem

    def top(self):
        if self.head is not None:
            return self.head.value
        
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.last = None

    # O(1)
    def size(self) -> int:
        return self.s1.size() + self.s2.size()
    
    # O(1)
    def enque(self, value: any) -> None:
       self.s1.push(value)
       self.last = value

    # O(1) @
    def deque(self) -> any:
        if self.s2.is_empty():
          self._transfer()

        return self.s2.pop()

    # O(1) @
    def front(self) -> any:
        if self.s2.is_empty():
          self._transfer()

        return self.s2.top()

    # O(1) 
    def rear(self) -> any:
       return self.last
    
    def _transfer(self) -> None:
        while self.s1.size() > 0:
            value = self.s1.pop()
            self.s2.push(value)



# https://leetcode.com/problems/implement-queue-using-stacks/
            

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.head = Node()
        self.length = 0

    def size(self) -> int:
        return self.length
    
    def is_empty(self) -> bool:
        return self.length == 0
    
    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        
        last_elem = self.top()
        self.head = self.head.next
        self.length -= 1
        return last_elem
       
    def top(self):
        if self.head is not None:
            return self.head.value

class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.last = None

    def push(self, x: int) -> None:
        self.s1.push(x)
        self.last = x

    def pop(self) -> None:
        if self.s2.is_empty():
            while self.s1.size() > 0:
                value = self.s1.pop()
                self.s2.push(value)
        return self.s2.pop()

    def peek(self):
        if self.s2.is_empty():
            while self.s1.size() > 0:
                value = self.s1.pop()
                self.s2.push(value)
        return self.s2.top()

    def empty(self) -> bool:
        return self.s1.is_empty() and self.s2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()