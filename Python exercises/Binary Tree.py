#BINARY TREE

class BinaryTree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    def insert_left(self,new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
    
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t
            self.counter += 1
            
    def insert_right(self,new_node):
         if self.right is None:
            self.right = BinaryTree(new_node)
            self.counter = 1
         else:
             t = BinaryTree(new_node)
             t.right = self.right
             self.right = t
             self.counter += 1
    
    def print_tree(self, level = 0):
        if self.right:
            self.right.print_tree(level + 1)
            print("    "*level+str(self.key))
        if self.left:
            self.left.print_tree(level + 1)

  

        


root = BinaryTree(10)
root.insert_left(6)
root.insert_right(15)
root.left.insert_left(4)
root.left.insert_right(8)
root.right.insert_left(12)
root.right.insert_right(18)

print("Original Tree: ")
root.print_tree()
print(root.counter_node())
       