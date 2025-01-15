class Stack:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return self.list == []
    
    def push(self, item):
        self.list.append(item)
    
    def peek(self):
        return self.list[len(self.list)-1] 
    
    def pop(self):
        if not self.is_empty():
            return self.list.pop(-1)
        return None
    
    def print(self):
        print(self.list)
    
    def size(self):
        return len(self.list)


class Stack_of_Plates:
    def __init__(self, limit=3):
        self.stack = Stack() 
        self.inner_stack = Stack()  
        self.limit = limit  #
    
    def is_empty(self):
        return self.stack.is_empty() and self.inner_stack.is_empty()
    
    def push_newstack(self):
        if not self.inner_stack.is_empty():
           
            self.stack.push(self.inner_stack)
            self.inner_stack = Stack()  
    
    def push_item_innerstack(self, item):
        if self.inner_stack.size() >= self.limit:
           
            self.push_newstack()
        self.inner_stack.push(item)
    
    def pop_newstack(self):
        
        return self.stack.pop()
    
    def pop_item_innerstack(self):
       
        return self.inner_stack.pop()
    
    def print(self):
       
        print("Inner Stack (Current Plates):")
        self.inner_stack.print()
    
    def print_stack(self):
        
        for inner in self.stack.list:
            inner.print()



sop = Stack_of_Plates(limit=3)


sop.push_item_innerstack(5)
sop.push_item_innerstack(5)
sop.push_item_innerstack(5)
sop.push_newstack() 
sop.push_item_innerstack(10)
sop.push_item_innerstack(10)


sop.print()
sop.print_stack()




        

    
    
