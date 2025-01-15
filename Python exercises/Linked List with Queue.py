# LINKED LIST WITH QUEUE
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
    
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    
    def set_data(self,new_data):
        self.data = new_data
    
    def set_next(self,new_next):
        self.next = new_next


class LinkedQueue:
    def __init__(self):
         self.front = None
         self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self,item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.set_next(new_node)
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        temp = self.front
        data = temp.get_data()
        self.front = self.front.get_next()

       
        if self.front is None:
            self.rear = None
        return data
    
    def print(self):
        if self.is_empty():
            print("Queue is empty!")
        traversal = self.front
        print("Queue: ", end="")
        while traversal:
            print(traversal.get_data(), end=" ")
            traversal = traversal.get_next()
        print()
        