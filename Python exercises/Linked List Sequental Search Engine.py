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


  
class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self,item):

        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
  
    def size(self):
        current = self.head
        count = 0
        while current !=None : 
            count += 1
            current = current.get_next()
        return count
    
    def search(self, item):
     counter = self.head
    
     while counter != None:
        if counter.get_data() == item:  
            return True
        counter = counter.get_next()  
    
     return False 
    
    def print(self):
         current  = self.head
         while current!=None:
          print(current.get_data(),end="-> ")
          counter  = current.get_next()

    def reverse(self):
        previous = None
        current = self.head
        while current != None:
         next_node = current.get_next()  
         current.set_next(previous)      
         previous = current            
         self.head = previous


    
              
            
          
   

    

        


  

linkedlist = LinkedList()

linkedlist.add(31)
linkedlist.add(77)
linkedlist.add(17)
linkedlist.add(93)
linkedlist.add(26)
linkedlist.add(54)

print(linkedlist.size())
print(linkedlist.search(17))
linkedlist.print()
linkedlist.reverse()
linkedlist.print()



