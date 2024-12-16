class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def append(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop(len(self.items)-1)
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def print(self):
        return print(self.items)



def reverse_string(input_string):
    # Initialize an empty stack (using a list)
    stack = []
    
    # Push each character of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Pop characters from the stack to form the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Get input from the user
user_input = input("Enter a string: ")

# Reverse the string using the stack
reversed_str = reverse_string(user_input)

# Output the reversed string
print("Reversed string:", reversed_str)


