from singly_link_list import*

class Stack:
    def __init__(self):
        self.__stack = Singly_link_list()

    def push(self,data):
        self.__stack.add_last(data) 

    def pop(self):
        if self.__is_empty:
            print("stack is empty")
            return
        self.__stack.delete_last()    

    def peak(self):
        self.__stack.peak_last()  

    def display(self):
        self.__stack.display_list() 

    def length(self):
        if self.__is_empty:
            print("Stack is empty")
            return
        return print(self.__stack.length())

    def __is_empty(self):
        if self.__stack.size == 0:
            return True

if __name__ == "__main__":
    s = Stack()
    s.pop()        
    s.display() 
    s.length()      