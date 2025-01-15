# LINKED LIST QUEUE
# NODE CLASS
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

# class Linked Queue
# Queue works on FIFO first in first out 
# Head - > Node data node next - > 
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

        # If the queue becomes empty, set rear to None as well
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
        

            

linked_queue = LinkedQueue()

linked_queue.enqueue(5)
linked_queue.enqueue(12)
linked_queue.enqueue(10)
linked_queue.print()
linked_queue.dequeue()
linked_queue.print()