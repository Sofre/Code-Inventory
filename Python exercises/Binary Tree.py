#BINARY TREE

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.counter = 0  # Initialize counter attribute
    
    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t
        self.counter += 1  # This could be used for tracking insertions
    
    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t
        self.counter += 1  # This could also track right insertions
    
    def print_tree(self, level=0):
        if self.right:
            self.right.print_tree(level + 1)
        print("    " * level + str(self.key))
        if self.left:
            self.left.print_tree(level + 1)

  

# Example usage:
root = BinaryTree(1)
root.insert_left(2)
root.insert_right(3)
root.insert_left(4)
root.right.insert_left(4)
root.right.insert_right(5)
root.left.insert_left(9)
root.left.insert_right(7)
root.left.insert_left(8)
root.print_tree()



  

        

       