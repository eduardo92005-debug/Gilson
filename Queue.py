class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.next = nxt
        
class Queue:
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__n = 0
    def is_empty(self):
        return self.__n == 0
    def __len__(self):
        return self.__n
    def enqueue(self, item):
        aux = Node(item,None)
        if self.is_empty():
            self.__start = aux
        else:
            self.__end.next = aux
        self.__end = aux
        self.__n += 1
    def dequeue(self):
        x = self.__start.item
        self.__start = self.__start.next
        self.__n -= 1
        if self.__n == 0:
            self.__end = None
        return x
        

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
print(q1.dequeue())
print(q1.dequeue())
