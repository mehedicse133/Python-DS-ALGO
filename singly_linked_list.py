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

    def add_at_any(self,position,data):
        new_node = Node(data)
        curr_node = self.head
        current_p = 0
        while True:
            if current_p == position:
               prev_node.next = new_node
               new_node.next =  curr_node
               self.size+=1
               break
            prev_node =  curr_node
            curr_node =  curr_node.next
            current_p += 1   
      
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

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def serach(self,item):
        temp = self.head
        while temp is not None:
            if temp.data == item:
                return print("Item Found") 
                
            return print("Item Not Found")
    

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev 

    

       



if __name__ == "__main__":
    l = Singly_link_list()
    l.add_last(8)
    l.add_first(5)
    l.add_first(4)
    l.add_first(1)
    l.add_last(9)
    # l.display_list()
    l.add_at_any(2,66)
    l.add_at_any(3,77)
    l.display_list()
    print(l.length())
    print('*'*20)
    l.reverse()
    l.display_list()
    
    
    
