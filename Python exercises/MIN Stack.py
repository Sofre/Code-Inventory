# MIN STACK

class Stack:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return self.list == []
    
    def push(self,item):
        self.list.append(item)
    
    def peek(self):
        return self.list[len(self.list)-1]
    
    def pop(self):
        self.list.pop(-1)
    
    def print(self):
        return print(self.list)
    
    

    


    


stack = Stack()



min_stack = Stack()
def push(item):
    stack.push(item)
    # Push to min_stack the current element or the min of current element and the last element in min_stack
    if min_stack.is_empty() or item <= min_stack.peek():
        min_stack.push(item)

# Pop an item from both the regular stack and the min stack
def pop():
    if not stack.is_empty():
        popped_item = stack.pop()
        if popped_item == min_stack.peek():
            min_stack.pop()

# Get the top item from the regular stack
def peek():
    return stack.peek() if not stack.is_empty() else None

# Get the minimum item from the min stack
def get_min():
    return min_stack.peek() if not min_stack.is_empty() else None



push(10)
push(5)
push(15)

print(get_min())