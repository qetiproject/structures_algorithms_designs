class Node:
   def __init__(self, value = None, next = None) -> None:
      self.value = value
      self.next = next
      
class LinkedQueue: #ჩავწეროთ მარჯვნიდან, წავიკითხოთ მარცხნიდან
    # O(1)
    def __init__(self) -> None:
       self.head = None
       self.tail = None # ბოლო ელემენტი
       self.length = 0

    # O(1)
    def size(self) -> int:
       return self.length

    # O(1) 
    def enqueue(self, value: any) -> None: # ჩამატება
        new_node = Node(value)
        if self.size() == 0:
           self.head = new_node
           self.tail = new_node
        else:
           self.tail.next = new_node
           self.tail = new_node
        self.length += 1

    # O(1) 
    def dequeue(self) -> any: #წაშლა ბოლო ელ და აბრუნებს ანუ მარცხნიდან პირველი
        if self.size() == 0:
          raise Exception("Queue is empty")
        elem = self.head.value
        self.head = self.head.next
        if self.head is None:
           self.tail = None
        self.length -= 1
        return elem
    
    # O(1)
    def front(self) -> any: # 1 ელ
        if self.size() == 0:
           raise Exception("Queue is empty")
        return self.head.value

    # O(1)
    def rear(self) -> any: # ბოლო ელ
        if self.size() == 0:
           raise Exception("Queue is empty")
        return self.tail.value