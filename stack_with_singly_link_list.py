from singly_link_list import*

class Stack:
    def __init__(self):
        self.__stack= Singly_link_list()

    def push(self,data):
        self.__stack.add_last(data)    

    def display(self):
        self.__stack.display_list()            


if __name__ == "__main__":
    s = Stack()
    s.push(20)        
    s.push(44)        
    s.push(55)        
    
    s.display()       