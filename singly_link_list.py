# Python Singly link list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_link_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.size+=1
        else:
            new_node.next = self.head
            self.head = new_node 
            self.size+=1

    def add_last(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.size+=1
        else:
            temp = self.head
            while temp:
                if temp.next == None:
                    temp.next = new_node
                    self.size+=1
                    return
                temp = temp.next
                
    def peak_head(self):
        return print(self.head.data) 

    def peak_last(self):
        temp = self.head
        while temp:
            if temp.next == None:
                return print(temp.data)
            temp = temp.next
            
    def delete_first(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
            self.size-=1

    def delete_last(self):
        if self.head == None:
            return
        else:
            temp = self.head
            while temp.next.next is not None: 
                temp = temp.next
            temp.next = None      
            self.size-=1
        
    def display_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
    def length(self):
        return self.size


if __name__ == "__main__":
    l = Singly_link_list()
    l.add_first(20)
    l.add_first(23)
    l.add_first(19)
    l.display_list()
    print('-'*20)
    l.delete_last()
    l.display_list()
    print('-'*20)