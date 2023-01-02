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

# enqueue(20)            
# enqueue(27)            
# enqueue(22)
# print(queue)
# length()  
# dequeue() 
# print(queue) 
# length() 

# Object oriented approach
class Queue:
    def __init__(self) -> None:
        self.queue = []
    

    def enqueue(self,val):
         self.queue.append(val)


    def dequeue(self):
        val =  self.queue.pop(0)
        print(val)

    def front_value(self):
        if is_empty:
            print("queue is empty")
        else:    
            return  self.queue[0]

    def print_queue(self):
        print( self.queue)

    def length(self):
        return len( self.queue) 

    def is_empty(self):
        if len(self.queue) == -1: 
            return  True
        return False 
    

if __name__ == "__main__":
    q = Queue()
    # s.peek()
    q.enqueue(44)
    q.enqueue(88)
    q.print_queue()
    q.dequeue()
    q.print_queue()

  
