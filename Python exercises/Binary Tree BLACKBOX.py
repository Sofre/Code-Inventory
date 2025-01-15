


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

