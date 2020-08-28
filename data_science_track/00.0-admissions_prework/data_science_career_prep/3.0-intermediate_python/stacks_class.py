class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)



"""
The def_init_(self) is the constructor: the part of the class that assigns
initial values to, or initializes, an instance of the class once it's made.
The def_init_ is a keyword and has to be there, but the self could have
been given a different name. All this constructor is doing is saying:
each time the class Stack is instantiated, just make an empty list and
call it stack. The self variable needs to be there just to keep things
local to the particular stack instance we're making when we instantiate the class.
"""
