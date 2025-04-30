# Build simple logic of the stack
class Stack:
    def __init__(self):
        self.s = []
    
    def puch(self,Value):
        self.s.append(Value)
    
    def pop(self):
        self.s.pop() if self.s  else ...
    
    def top(self):
        print(self.s[-1])
    
    def peek(self):
        return (self.s[-1])
    
    def isempty(self):
        return not(bool(len(self.s)))

    def getmin(self):
        if self.s:
            return sorted(self.s)[0]

    def show(self):
        return self.s

lis=Stack()

lis.puch(12)
lis.puch(11)
lis.puch(13)
lis.puch(133)
lis.puch(14)
lis.puch(111)
print(lis.getmin())
print(lis.show())

#--------------use deque in stack for performance--------------# 

# cuz its use the linked list to avoid the shifting in the list in python
from collections import deque

s=deque()
print(dir(s))
print(s.__doc__)
