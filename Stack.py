class ErrorHandling:
    " A class to handle errors"
class Empty(ErrorHandling, Exception):
    "A subclass error"
class Stack:
    "Implements a stack in python code"
    def __init__(self):
        self.__stack = []
    def push(self, item):
        " Insert a element to final position"
        self.__stack += [item]
    def pop(self):
        " Remove the top element"
        return self.__stack.pop()  
    def __len__(self):
        "Returns the size the stack"
        return len(self.__stack)
    def is_empty(self):
        "Check if stack is empty"
        return len(self.__stack) == 0
    def peek(self):
        " Returns the top element of the stack"
        if self.is_empty():
            raise Empty("Stack is Empty!")
        return self.__stack[-1]
    
        
