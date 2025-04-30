# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None


# head=Node(100)
# th2=Node(200)
# th3=Node(300)
# th4=Node(400)
# th5=Node(500)

# head.next = th2
# th2.next= th3
# th3.next= th4
# th4.next= th5


# print(head.next.next.next.next.next.data)

# while head != None :
#     print(head.data)
#     head=head.next


# كده بخليه يطلب أحط النود الي بعدها على طول و الا هيعملها None عكس الي فوق ملهاش نود بعدها و لازم أخدهم أربطهم ببعض 

class Node :
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert_beging(self,data):
        node = Node(data,self.head)
        self.head = node
        self.len += 1

    def insert_end(self, data):
        node = Node(data)
        if self.head is None :
            self.head = node
            self.len += 1
            return
        current = self.head
        while current.next :
            current = current.next
        current.next = node
        self.len += 1

    def insert_values(self, data:list):
        for i in data :
            self.insert_end(i)

    def insert_at(self, data, index:int):
        if index == 0 :
            self.insert_beging(data)
            return
        elif index < 0 or index >= self.len :
            raise ValueError("Out of range.")
        current = self.head
        count = 1
        while index > count :
            current = current.next
            count += 1
        node = Node(data, current.next) # خليت النود الي حطتها بتشاور على النود الي هتاخذ مكناها 
        current.next = node # هنا كده خليت النود الي قبل النود تشاور عالنود الجديده بدل القديمه الي طلعت قدام
        self.len += 1

    def insert_after_value(self, data_after, data_to_insert):
        current = self.head
        for i in range(len(self)):
            if current.data == data_after :
                self.insert_at(data_to_insert, i+1)
                return
            else :
                current = current.next
        print(f"The {data_after} is not found in the ll")

    def remove_at(self, index:int):
        if index >= self.len or index < 0 :
            raise Exception(f"out of range the number of elements is {self.len}")
        if index == 0 :
            self.head = self.head.next # self.head --> 2th Node and left 1th Node After that the Garbage Collector remove 1th Node
            return
        count = 1
        current = self.head
        while index > count : # هخلي المؤشر الي بيئشر عالنود الي هحذفها الي طالع من المود الي قبلها يشاور عالنود الي بعدها 
            count += 1
            current = current.next
        current.next = current.next.next # current.next == The Node that before the Node what will be removed
        self.len -= 1

    def remove_by_value(self, data):
        current = self.head
        for i in range(len(self)):
            if current.data == data:
                self.remove_at(i)
                return
            else :
                current = current.next
        print(f"The {data} is not found.")

    def __len__(self):
        return self.len

    def print(self):
        if self.head is None :
            print("linked list is empty.")
            return
        current = self.head # To Avoid mistakes or changes in the real ll
        while current != None :
            print(f"{current.data}--> ", end="")
            current = current.next
        print(None)

if __name__ == "__main__" :
    queu = LinkedList()
    queu.insert_values(["Abdalrhman", "Mohamed", "Abdalla", "Ali"])
    queu.print()
    print(len(queu))
    
    # queu.remove_at(2)
    
    queu.insert_at("Hassan", 0)
    queu.insert_at("Bakr", 4)
    queu.print()
    
    queu.remove_by_value("Bakr")
    queu.print()
    print(len(queu))