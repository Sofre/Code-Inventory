class Node:
    #Class Node for setters getters for data and link 
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


    #Class Linked List for the list and mechanics for setting header
class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def add(self,item):

        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    # Lenght method
    def size(self):
        current = self.head
        count = 0
        while current !=None : 
            count += 1
            current = current.get_next()
        return count
    
   

    

        


  

linkedlist = LinkedList()

linkedlist.add(31)
linkedlist.add(22)
linkedlist.add(18)
linkedlist.add(99)
linkedlist.add(50)
linkedlist.add(11)

print(linkedlist.size())




