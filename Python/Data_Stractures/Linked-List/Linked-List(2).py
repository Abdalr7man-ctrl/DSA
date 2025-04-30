# Doubly linked list
# TODO : All 

class DoubleNode :
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList :
    def __init__(self, head=None, tail=None):
        self.head = head # أول نود  
        self.tail = tail # أخر نود
        self.len = 0
    
    def insert_beging(self,data):
        node = DoubleNode(data,self.head,None)
        if self.len > 0 :
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self.len += 1

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        current = self.head
        for i in range(self.len):
            print(f"{current.data} <---> ",end="")
            current = current.next
        print(None)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        current = self.tail
        for i in range(self.len):
            print(f"{current.data} <---> ",end="")
            current = current.prev
        print(None)

if __name__ == "__main__" :
    ll = DoublyLinkedList()
    print(ll.head)
    ll.insert_beging("Abdo")
    ll.insert_beging("Bakr")
    ll.insert_beging("Hassan")
    ll.insert_beging("Moamen")
    ll.insert_beging("youssef")
    print(ll.len)
    ll.print_forward()
    ll.print_backward()
