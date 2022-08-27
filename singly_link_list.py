# Python Singly link list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly_link_list:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


l = Singly_link_list()
l.add_first(20)
l.add_first(23)
l.add_first(10)
l.display_list()