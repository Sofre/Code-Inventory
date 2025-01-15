# PALINDROM LINKED LIST
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
        item = Node(item)
        item.set_next(self.head)
        self.head = item
        
    
    def delete(self):
        if self.is_empty():
            print("Linked List is empty")
        else:
           get_item = self.head.get_data()
           self.head = self.head.get_next()
           print(f"Item deleted is {get_item}")
    
    def size(self):
        counter = 0
        current = self.head
        while current is not None:
            counter+=1
            current = current.get_next()
        return counter
    
    def print(self):
        current = self.head
        print_list = []
        while current is not None:
            print_list.append(current.get_data())
            current = current.get_next()
        print(print_list)
    
    def isPalindrom(self):
        if not self.head or not self.head.next:
            return True
        

        slow , fast = self.head , self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        while slow:
          next_node = slow.next
          slow.next = prev
          prev = slow
          slow = next_node  

        
        left,right = self.head,prev

        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True
    
        

    
            

linkedlist = LinkedList()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)


print(linkedlist.isPalindrom())

