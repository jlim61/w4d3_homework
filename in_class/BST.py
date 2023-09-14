from Node import Node

'''
In tree there is starting node. That has a right or left value. Any additional node on it in a binary search tree must be
ordered. adding the node has the smaller one go on left and bigger on right. so if you had a starting of 8. if you try
to add a 3, that would go on left. if you try to add 10, that goes on the right

in binary search tree, the head node is root node. just different wording.
'''

class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def __repr__(self):
        return f'<BST: {self.root}'
    
    def add_node(self, value, current_node = None):
        if not current_node:
            current_node = self.root
        if value > current_node.value:
            if current_node.right:
                self.add_node(value, current_node.right)
            else:
                current_node.right = Node(value)
        elif value < current_node.value:
            if current_node.left:
                self.add_node(value, current_node.left)
            else:
                current_node.left = Node(value)

    def search(self, value, current_node = None):
        if not current_node:
            current_node = self.root
        if value > current_node.value:
            if current_node.right:
                return self.search(value, current_node.right)
        elif value < current_node.value:
            if current_node.left:
                return self.search(value, current_node.left)
        else:
            return current_node
        print(f'Node: {value} not found')
        return False

    def get_min(self):
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node

    def get_max(self):
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node
    
    def get_max_recursion(self, current_node = None):
        if not current_node:
            current_node = self.root
        if current_node.right:
            current_node = current_node.right
            return self.get_max_recursion(current_node)
        return current_node
    
    def get_min_recursion(self, current_node = None):
        if not current_node:
            current_node = self.root
        if current_node.left:
            current_node = current_node.left
            return self.get_min_recursion(current_node)
        return current_node
    # instead of sorting, we need to store them in some kind of list first to create the listed sort for hw
    def print_sorted(self, current_node = None):
        if not current_node:
            current_node = self.root
        if current_node.left:
            self.print_sorted(current_node.left)
        print(current_node.value)
        if current_node.right:
            self.print_sorted(current_node.right)

    def print_reverse(self, current_node = None):
        if not current_node:
            current_node = self.root
        if current_node.right:
            self.print_reverse(current_node.right)
        print(current_node.value)
        if current_node.left:
            self.print_reverse(current_node.left)


    
bst = BinarySearchTree(100)
bst.add_node(125)
bst.add_node(50)
bst.add_node(115)
bst.add_node(130)
bst.add_node(75)
bst.add_node(25)
bst.add_node(110)
bst.add_node(120)
print(bst)
# 
# print(bst)
# print(bst.root) # looking at main root
# print(bst.root.right) # looking at 125: 100 > 125
# print(bst.root.left) # looking at 50: 100 > 50
# print(bst.root.right.right) # looking at 130: 100 > 125> 130
# print(bst.root.right.left) # looking at 115: 100 > 125> 115
# print(bst.root.left.right) # looking at 75: 100 > 50 > 75

# print(bst.search(75), 'test search')
# print(bst.get_max(), 'max')
# print(bst.get_min(), 'min')
# print(bst.get_max_recursion(), 'max rec')
# print(bst.get_min_recursion(), 'min rec')
# print(bst.print_sorted(), 'sorted method')
# print(bst.print_reverse(), 'reverse method')