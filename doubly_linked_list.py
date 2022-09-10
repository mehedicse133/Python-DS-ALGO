# Python Doubly linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doublylist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_at_first(self,data):
        new_node = node(data)            
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            
        else:
            
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node.next

           
            

            # new_node.next = self.head
            # self.head.prev = new_node
            # self.tail = new_node.next
            # # self.tail.prev = new_node
            # self.head = new_node

    def display(self):
        temp = self.head          
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def peak_first(self):
        return self.head

    def peak_last(self):
        return self.tail

    def reverse(self):
        tail = self.tail
        while tail.prev is not None:
            print(tail.prev.data)
            tail = tail.prev



if __name__ == "__main__":
    l = doublylist() 
    l.add_at_first(21)          
    l.add_at_first(27)          
    l.add_at_first(88)          
    l.add_at_first(11)          
    l.add_at_first(66)          
            
    l.display()
 
  
   

    
