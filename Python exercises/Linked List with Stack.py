class Node:
    def __init__(self, data):
        self.data = data  # Data in the node
        self.next = None  # Pointer to the next node

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
        self.head = None  # Head points to the top of the stack (top of the linked list)
        
    def is_empty(self):
        return self.head is None  # If the head is None, the stack is empty

    def push(self, item):
       
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            top_node = self.head
            self.head = self.head.get_next()  # Move the head to the next node
            return top_node.get_data()  # Return the data of the popped node
        else:
            return None  # If the stack is empty, return None

    def peek(self):
        if not self.is_empty():
            return self.head.get_data()  # Return the data of the top node
        else:
            return None  # If the stack is empty, return None

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
        print(stack_list)  # Print the stack from top to bottom

# Example usage:
stack = LinkedStack()

stack.push(20)
stack.push(30)
stack.push(40)

print("Stack after pushes:")
stack.print_stack()  

print("Peek top element:", stack.peek())  # Output: 40

print("Pop top element:", stack.pop())  # Output: 40
stack.print_stack()  # Output: [30, 20]

print("Stack size:", stack.size())  # Output: 2

print("Is stack empty?", stack.is_empty())  # 

stack.pop()
stack.pop()
print("Is stack empty?", stack.is_empty())  
