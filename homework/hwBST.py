from hwNode import Node

'''
In tree there is starting node. That has a right or left value. Any additional node on it in a binary search tree must be
ordered. adding the node has the smaller one go on left and bigger on right. so if you had a starting of 8. if you try
to add a 3, that would go on left. if you try to add 10, that goes on the right

in binary search tree, the head node is root node. just different wording.
'''

class BinarySearchTree:

    def __init__(self, root_value):

        self.root = Node(root_value)
        self.sorted_linked_list = []

    def __repr__(self):
        # print(f'{self.sorted_linked_list}')

        # output = '<BinarySearchTree: '
        # for num in self.sorted_linked_list:
        #     output += f'{num} -> '
        # return output.rstrip(' -> ')

        return f'<BinarySearchTree: {" -> ".join(str(num) for num in self.sorted_linked_list)}>'
    
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


# -----------------------------------------------------------------------------------


# README!
# I wasn't sure if the prompt wanted me to instantiate the binary search tree with the list
# i.e: bst = BinarySearchTree([8,6,2,9,10,7])
# because then it says to add nodes and have it iterate over the rest of the list which I'm not sure if that
# means I'm supposed to run the function with the list in it as well
# i.e: bst.Add_Nodes([8,6,2,9,10,7])

# I just built into my code that it will overwrite the self.root so that I only add the list into the Add_Nodes method.




# ------------------------------ADD Nodes Method-----------------------------------------

    def hw_add_nodes(self, alist_value, current_node = None):
        if not current_node:
            self.root = Node(alist_value[0])
            current_node = self.root
            print(current_node)
        for num in alist_value[1:]:
            self.helper(num, current_node)

# Helper Function (Actually Does the Adding to Bypass my List Assumption Input from hw_add_nodes)

    def helper(self, num_check, current_node):
        

# -----------Adding Smaller Number to Left------------------------------------

        if num_check < current_node.value:
            print(f'{num_check} - to the left')
            if current_node.left:
                self.helper(num_check, current_node.left)
            else:
                current_node.left = Node(num_check)

# -----------Adding Smaller Number to Right------------------------------------

        elif num_check > current_node.value:
            print(f'{num_check} - to the right')
            if current_node.right:
                self.helper(num_check, current_node.right)
            else:
                current_node.right = Node(num_check)

# --------================---In-Order Traversal------------------------------------

    def in_order_traversal(self, current_node = None):
        if not current_node:
            current_node = self.root
        if current_node.left:
            self.in_order_traversal(current_node.left)
        self.sorted_linked_list.append(current_node.value)
        if current_node.right:
            self.in_order_traversal(current_node.right)
            

# ------------Used to Test hw_add_nodes and helper Methods------------------
    
# bst = BinarySearchTree('test')
# print(bst.root)
# bst.hw_add_nodes([8,6,2,9,10,7])
# print('seeing if code did an overwrite on self.root')
# print(bst.root)
# print('seeing if hw_add_sort added next number [in this case it is 6 and should be .left]')
# print(bst.root.left)
# print('seeing if hw_add_sort added next number [in this case it is 2 and should be .left.left]')
# print(bst.root.left.left)
# print('seeing if hw_add_sort added next number [in this case it is 9 and should be .right]')
# print(bst.root.right)
# print('seeing if hw_add_sort added next number [in this case it is 10 and should be .right.right]')
# print(bst.root.right.right)
# print('seeing if hw_add_sort added next number [in this case it is 7 and should be .left.right]')
# print(bst.root.left.right)

# ---------Used to Test in_order_traversal Method------------------

bst = BinarySearchTree('test')
bst.hw_add_nodes([8,6,2,9,10,7])
bst.in_order_traversal()
print(bst)
# bst.in_order_traversal()
# print(bst.sorted_linked_list)