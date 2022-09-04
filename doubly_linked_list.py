# Implement doubly link list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_Llist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,data): 
        new = Node(data) 
        if self.head == None:         
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new




if __name__ == "__main__":


    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    list = doubly_Llist()

    list.head = node1
    list.tail = node1

    node1.prev =list.head.prev

    node1.next =node2
    list.tail = node2
    print(list.tail.data)

    node2.next = node3
    node2.prev = node2
    list.tail =node3
    node3.prev = node2
    print(list.tail.data)
    print(list.tail.prev.data)
   

    
