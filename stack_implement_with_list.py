# Functional approch

stack = []

def add(val):
    stack.append(val)
def pop():
    val = stack.pop()
    print(val)    
def peek():
    return stack[-1]
def length():
    return len(stack) 
def is_empty():
    if len(stack)== -1:
        return  True
    return False           


# add(10)        
# add(20)
# add(30)
# add(40)
# add(888)
# print(stack)
# print(peek())
# print(len(stack))
# print(is_empty()) 


# Object oriented approach
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def add(self,val):
        self.stack.append(val)

    def pop(self):
        val = self.stack.pop()
        print(val)

    def peek(self):
        if is_empty:
            print("stack is empty")
        else:    
            return self.stack[-1]

    def print_stack(self):
        print(self.stack)

    def length(self):
        return len(self.stack) 

    def is_empty(self):
        if len(self.stack) == -1: 
            return  True
        return False 


if __name__ == "__main__":
    s = Stack()
    # s.peek()
    s.add(44)
    s.add(88)
    # s.add(44)
    # s.add(44)
    s.print_stack()
