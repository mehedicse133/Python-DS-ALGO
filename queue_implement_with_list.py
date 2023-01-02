# Functional approach
queue = []

def enqueue(val):
    queue.append(val)

def dequeue():
    val = queue.pop(0)
    print(val) 

def peek():
    return queue[0]

def length():
    return print(len(queue) )

def is_empty():
    if len(queue)== -1:
        return  True
    return False

enqueue(20)            
enqueue(27)            
enqueue(22)
print(queue)
length()  
dequeue() 
print(queue) 
length()        