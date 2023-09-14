from hwNode import Node

'''
first node is head node

last node is tail node
'''

class LinkedList:

    def __init__(self, head_value):
        self.head = Node(head_value)

    def __repr__(self):
        # output = '<LinkedList: '
        # for node in self:
        #     output += f'{node.value} -> '
        # return output.rstrip(' -> ')
        return f'<LinkedList: {" -> ".join(node.value for node in self)}>'
    
    def __iter__(self):
        current_node = self.head
        while current_node.right:
            yield current_node
            current_node = current_node.right
        yield current_node
    
    def append_node(self, value):
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = Node(value)

    def insert(self, neighbor, value):
        for node in self:
            if node.value == neighbor:
                next_node = node.right
                node.right = Node(value)
                node.right.right = next_node
                return
        print(f'{neighbor} not in LinkedList')

    def update_head(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.right = old_head
        # new_head = Node(value)
        # new_head.right = self.head
        # self.head = new_head

    def search(self, value):
        for node in self:
            if node.value == value:
                return node
        return False

    def get_tail(self):
        # when you use a for loop and you do pass, it holds onto the last value it looked at
        for node in self:
            pass
        return node
        # current_node = self.head
        # while current_node.right:
        #     current_node = current_node.right
        # return current_node


    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.right
            return
        for node in self:
            # the node.right is a truthy check like "if node.right". It's essentially checking first if there is a node.right
            if node.right and node.right.value == value:
                node.right = node.right.right
                return


linkedlist = LinkedList('Monday')
# linkedlist.append_node('Tuesday')
# linkedlist.append_node('Wednesday')
# linkedlist.insert('Wednesday','Thursday')
# linkedlist.append_node('Friday')
# # add sunday to beginning
# linkedlist.update_head('Sunday')
# print(linkedlist)

# print(linkedlist.get_tail())

# linkedlist.remove("Wednesday")

# print(linkedlist.search('Monday'))
# print(linkedlist.search('Friday'))



# for node in linkedlist:
    # print(node)
    # print(linkedlist.search(node.value))