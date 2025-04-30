# Queue

- Queue :  is a linear abstract data structure that stores items in a First In First Out (FIFO) manner.

## Time Complexity & Space Complexity

- Enqueue: Adds an item to the queue. – Time Complexity : O(1)
- Dequeue: Removes an item from the queue. – Time Complexity : O(1)
- Rear: Get the last item from queue – Time Complexity : O(1)
- Peek: Returns the first element in the queue. – Time Complexity : O(1)
- isEmpty: Checks if the queue is empty. – Time Complexity : O(1)
- Size: Finds the number of elements in the queue. – Time Complexity : O(1)
---
## Implement a Queue in Python

- Queues can be implemented by using arrays or linked lists.
- Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

Reasons to implement queues using arrays:

    Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
    Easier to implement and understand: Using arrays to implement queues require less code than using linked lists, and for this reason it is typically easier to understand as well.

Reasons for not using arrays to implement queues:

    Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements. And resizing an array can be costly.
    Shifting cost: Dequeue causes the first element in a queue to be removed, and the other elements must be shifted to take the removed elements' place. This is inefficient and can cause problems, especially if the queue is long.
    Alternatives: Some programming languages have built-in data structures optimized for queue operations that are better than using arrays.
---
Reasons for using linked lists to implement queues:

    Dynamic size: The queue can grow and shrink dynamically, unlike with arrays.
    No shifting: The front element of the queue can be removed (enqueue) without having to shift other elements in the memory.

Reasons for not using linked lists to implement queues:

    Extra memory: Each queue element must contain the address to the next element (the next linked list node).
    Readability: The code might be harder to read and write for some because it is longer and more complex.

### 1-Implementation using list
- [See there from line 1:46 ](./Queue.py)

### 2-Implementation using collections.deque
- It uses a linked list internally to build queues and is implemented in C.
- [See there from line 46:65 ](./Queue.py)

### 3-Implementation using queue.Queue
- It uses `collections.deque` and adds threading for thread safety. It is implemented in Python
- [See there from line 65](./Queue.py)
