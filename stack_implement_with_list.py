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

add(10)        
add(20)
add(30)
add(40)
add(888)
print(stack)
print(peek())
print(len(stack))
print(is_empty()) 



