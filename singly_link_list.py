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

    def peak_last(self):
        temp = self.head
        while temp:
            if temp.next == None:
                return print(temp.data)
            temp = temp.next
              
    def peak_head(self):
        return print(self.head.data) 
    
    def delete_first(self):
        if self.head == None:
            return
        else:
            temp = self.head
            self.head = temp.next

    def delete_last(self):
        temp = self.head
        c = 0
        while temp:
            c += 1
            temp = temp.next
        print(c)



    def display_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next





if __name__ == "__main__":
    l = Singly_link_list()
    l.add_first(20)
    l.add_first(23)
    l.add_first(19)
   
    l.display_list()
    print('-'*20)
    l.delete_last()

    # print('-'*20)
    # l.peak_head()
    # print('-'*20)
    # l.peak_last()


    # l.delete_first()
    # l.display_list()
    # print('-'*20)
    # l.display_list()
    # print('-'*20)
    # l.delete_first()
    # l.display_list()