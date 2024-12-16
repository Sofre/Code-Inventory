class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
  
    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            # Inserting new value where it pushes old value as the child of the new value
            t = BinaryTree(new_node)
            t.left = self.left # gives old value to new child
            self.left = t # new value is given to left child
    
    def insert_right(self, new_node):
        # Same as insert_left
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t
        
    def print_tree(self, level=0, prefix="Root: ", spacing="    "):
        
        print(f"{spacing * level}{prefix}{self.key}")
        
    
        if self.left:
            self.left.print_tree(level + 1, "L--- ", spacing)
        if self.right:
            self.right.print_tree(level + 1, "R--- ", spacing)

    def preorder(self):
        print(self.key, end =" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
       
        if self.right:
            self.right.postorder()
       
        print(self.key,end=" ")

    def inorder_traversal(self):
       
        if self is None:
            return
  
        if self.left:
            self.left.inorder_traversal()
   
        print(self.key, end=" ")
      
        if self.right:
            self.right.inorder_traversal()

  
    





root = BinaryTree(1)
root.insert_left(2)
root.insert_right(3)
root.left.insert_left(4)
root.left.insert_right(5)
root.right.insert_left(6)
root.right.insert_right(7)
root.print_tree()
print("Preorder:",end=" ")
root.preorder()
print(" , Postorder:",end=" ")
root.postorder()
print("  , Inorder:",end=" ")
root.inorder_traversal()