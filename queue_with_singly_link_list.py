from singly_link_list import*

class Queue:
    def __init__(self) -> None:
        self.__queue = Singly_link_list()

    def enqueue(self,data):
        self.__queue.add_last(data)  

    def dequeue(self):
        self.__queue.delete_first() 

    def display_queue(self):
        self.__queue.display_list()

    def size(self):
        return self.__queue.length()   

if __name__ == "__main__":
    q= Queue() 
    q.enqueue('first')
    q.enqueue('second')
    q.enqueue('third')
    print( q.size())
    q.display_queue()     
    print('-'*20)
    q.dequeue()
    q.display_queue() 
