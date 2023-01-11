class Node:
    def __init__(self,val) -> None:
        self.left = None
        self.right = None
        self.val = val 


class BinaryTree:
    def __init__(self):
        self.root = None 

    def insert(self,val):
        newNode = Node(val)
        if self.root == None:
            self.root = newNode
