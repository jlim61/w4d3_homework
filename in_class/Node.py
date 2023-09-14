class Node:

# each node has a value. each node has a connection to another node
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f'<Node: {self.value}>'
    
# node = Node('Monday')

# node2 = Node('Tuesday')

# node.right = node2 # setting Monday right to Tuesday

# node3 = Node("Wednesday")

# node2.right = node3 # setting Tuesday right to Wednesday

# node4 = Node('Thursday')

# node3.right = node4 # setting Wednesday right to Thursday

# node5 = Node('Friday')

# node4.right = node5 # setting Thursday right to Friday

# node6 = Node('Saturday')

# node5.right = node6 # setting Friday right to Saturday

# node7 = Node('Sunday')

# # the line below allows the link to move forward and backward
# # node.left = node7

# node7.right = node


# '''
#     [Sunday]>[Monday]>[Tuesday]>[Wednesday]>[Thursday]>[Friday]>[Saturday]

# '''

# print(node7) # Sunday
# print(node7.right) # Monday
# print(node.right) # Tuesday
# print(node.right.right) # Wednesday
# print(node.right.right.right) # Thursday
# print(node.right.right.right.right) # Friday
# print(node.right.right.right.right.right) # Saturday