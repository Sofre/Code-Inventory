#Binary Search Tree
class BinarySearchTree:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self,new_node):
        if new_node<self.key:
            if self.left is None:
                self.left  = BinarySearchTree(new_node)
            else:
                self.left.insert(new_node)
        elif new_node>self.key:
            if self.right is None:
             self.right = BinarySearchTree(new_node)
            else:
                self.right.insert(new_node)
                
    def print_tree(self, level = 0):
        if self.right:
            self.right.print_tree(level+1)
        print("  " * level + str(self.key))
        if self.left:
            self.left.print_tree(level+1)

    def search_engine(list,item):
        first = 0
        last = len(list) - 1
        found = False
        while first < last and not found:
                midpoint = (first+last)//2
        if(list[midpoint]==item):
                found=True
        else:
             if item<list[midpoint]:
                  last = midpoint-1
             else:
                  first = midpoint+1
        return found
    

    def preorder(self):
        print(self.key, end =" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    

    
    def search_tree(self, item):
    # Check if the current node's key matches the item
        if self.key == item:
          return True
    
    # If the item is smaller than the current node's key, search the left subtree
        if item < self.key and self.left:
           return self.left.search_tree(item)
    
    # If the item is greater than the current node's key, search the right subtree
        if item > self.key and self.right:
          return self.right.search_tree(item)
    
    # If the item is not found in either the left or right subtrees
        return False



















root = BinarySearchTree(10)
root.insert(6)
root.insert(15)
root.insert(4)
root.insert(8)
root.insert(12)
root.insert(8)
root.print_tree()
print(root.search_tree(6))
