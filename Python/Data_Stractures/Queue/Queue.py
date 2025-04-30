#--------(Queue Implementation using list)-------------#

class ListQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        """add item from the front"""
        self.queue.insert(0, element)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        """return first elemnt was put"""
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if self.queue:
            return False
        return True

my_queue = ListQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue.queue)
print(my_queue.peek())
print(my_queue.isEmpty())
print(my_queue.size())

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

print(my_queue.queue)
# print(my_queue.peek()) # will give error cuz the list empty
print(my_queue.isEmpty())
print(my_queue.size())


#--------(Implementation using collections.deque)-------------#
print("-" * 40)
from collections import deque

my_queue1 = deque()
my_queue1.appendleft(1)
my_queue1.appendleft(2)
my_queue1.appendleft(3)

print(my_queue1)
print(len(my_queue1))

print(my_queue1.pop())
print(my_queue1.pop())
print(my_queue1.pop())

print(my_queue1)


#--------(Implementation using queue.Queue)-------------#
print("-" * 40)
from queue import Queue

my_queue2 = Queue(12)

my_queue2.put(1)
my_queue2.put(2)
my_queue2.put(3)
print(my_queue2.queue)
print(my_queue2.empty())
print(len(my_queue2.queue))

print("-" * 40)

my_queue2.get()
my_queue2.get()
my_queue2.get()
print(my_queue2.queue)
print(my_queue2.empty())
