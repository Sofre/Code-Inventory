# FINALS 1
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class LinkedStack:
    def __init__(self):
        self.head = None  
        
    def is_empty(self):
        return self.head is None  

    def push(self, item):
       
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            top_node = self.head
            self.head = self.head.get_next()  
            return top_node.get_data()  
        else:
            return None  

    def peek(self):
        if not self.is_empty():
            return self.head.get_data() 
        else:
            return None  

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def print_stack(self):
        current = self.head
        stack_list = []
        while current is not None:
            stack_list.append(current.get_data())
            current = current.get_next()
        print("".join(reversed(stack_list)))

    def clear_copycats(self):
     current = self.head
     seen_data = set()  # set() data struc for seen data.
     previous = None   # used to mark data that has been checked or for duplicates

     while current is not None:
        if current.get_data() in seen_data:
            previous.set_next(current.get_next()) # previous here is used to store data that is duplicate tehnicly removing it so we irritate onwards
        else:
            
            seen_data.add(current.get_data())
            previous = current # current data becomes previous so it helps with irretation, this is so in any option of if or else 
        current = current.get_next()

               




user_string = input("Input a string: ")

linked_stack = LinkedStack()
for x in user_string:
    linked_stack.push(x)



linked_stack.print_stack()


linked_stack.clear_copycats()



linked_stack.print_stack()
