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
        self.counter = 1

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        
        else:
            # Inserting new value where it pushes old value as the child of the new value
            t = BinaryTree(new_node)
            t.left = self.left  # gives old value to new child
            self.left = t  # new value is given to left child
        

    def insert_right(self, new_node):
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

    def count_nodes(self):
        # Recursively count the nodes in the tree
        count = 1  # Count the current node
        if self.left:
            count += self.left.count_nodes()  # Add the left subtree node count
        if self.right:
            count += self.right.count_nodes()  # Add the right subtree node count
        return count


def build_tree(ROOT, L, R, L_R, R_L, R_R):
    root = BinaryTree(ROOT)
    root.insert_left(L)  # insert L to the left of root
    root.insert_right(R)  # insert R to the right of root
    root.left.insert_left(L_R)  # insert L_R to the left of L
    root.left.insert_right(R_L)  # insert R_L to the right of L
    root.right.insert_left(R_R)  # insert R_R to the left of R
    root.print_tree()  # print the tree structure
    print(root.count_nodes())  # print the node count


# Build a tree
build_tree("a", "b", "c", "d", "e", "f")
