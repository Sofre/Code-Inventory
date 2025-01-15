# BINARY TREE

class BinaryTree:
    def __init__(self,key):
        self.key =  key 
        self.left = None 
        self.right = None 

    def insert_left(self,item):
        if self.left is None:
            self.left = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.left = self.left
            self.left = t
    
    def insert_right(self,item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.right = self.right
            self.right = t
    
    def print(self,level=0,prefix="Root: " ,spacing="    "):
        print(f"{level * spacing } {prefix} {self.key}")

        if self.left:
            self.left.print(level+1,"L---",spacing)
        if self.right:
            self.right.print(level+1,"R---",spacing)

    def preorder(self):
        print(self.key,end=" ")

        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    
    def inorder(self):

        if self.left:
            self.left.inorder()
        print(self.key,end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key,end=" ")
    
    def sort_tree(self):
        # Step 1: Collect all values in the tree
        values = self._collect_values()

        # Step 2: Sort values in descending order
        values.sort(reverse=True)

        # Step 3: Rebuild the tree using sorted values
        self._rebuild_tree(values)

    def _collect_values(self):
       # collects values in a list 
        values = []
        if self.left:
            values.extend(self.left._collect_values())
        values.append(self.key)
        if self.right:
            values.extend(self.right._collect_values())
        return values

    def _rebuild_tree(self, sorted_values):
        # Base case once data has been rebuild in tree , sorted_values will have no data
        if not sorted_values:
            return None

        # The root node will be the first element in the sorted list
        self.key = sorted_values.pop(0)

        # Rebuild the left subtree (larger values)
        if sorted_values:
            self.left = BinaryTree(sorted_values.pop(0))
            self.left._rebuild_tree(sorted_values)

        # Rebuild the right subtree (smaller values)
        if sorted_values:
            self.right = BinaryTree(sorted_values.pop(0))
            self.right._rebuild_tree(sorted_values)







    


tree = BinaryTree(5)
tree.insert_left(2)
tree.insert_right(3)
tree.left.insert_right(10)
tree.left.insert_left(18)
tree.print()

tree.preorder()
print()
tree.inorder()
print()
tree.postorder()

tree.sort_tree()
tree.print()