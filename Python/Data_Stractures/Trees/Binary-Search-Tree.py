# ---------------------(Binary Search Tree)---------------------#

mytree = """        5
                    / \
                    0   10
                    /      \
                -5       45
                /        /
                -10      15
                        \
                        20
                            \  
                            30   
                            /
                        25  
"""

class Bst :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        
        if data == self.data:
            return None
        elif data > self.data :
            if not self.right :
                self.right = Bst(data)
            else :
                self.right.add_child(data)
        elif data < self.data :
            if not self.left :
                self.left = Bst(data)
            else :
                self.left.add_child(data)

    def in_order(self):  # left sub Tree --> root --> right sub Tree
        element=[]
        # visit left sub tree 
        if self.left :
            element+=self.left.in_order()
        # visit root node 
        element.append(self.data)
        # visit right sub tree 
        if self.right :
            element+=self.right.in_order()
        return element

    def post_order_traversal(self): # left sub Tree --> right sub Tree --> root
        element=[]
        if self.left :
            element += self.left.post_order_traversal()
        if self.right :
            element += self.right.post_order_traversal()
        element.append(self.data)
        return element

    def  pre_order_traversal(self): # root --> left sub Tree --> right sub Tree
        element=[]
        element.append(self.data)
        if self.left :
            element += self.left.pre_order_traversal()
        if self.right :
            element += self.right.pre_order_traversal()
        return element

    def search(self, val):
        if self.data == val :
            return self.data
        elif val > self.data :
            if self.right :
                return self.right.search(val)
        elif val < self.data :
            if self.left :
                return self.left.search(val)
        return False

    def find_max(self):
        current = self # عمل مؤشر جديد على العقد لمنع الألتباس و تجنبا للأخطاء 
        while current.right is not None :
            current = current.right
        return current.data

    def find_min(self): 
        current = self # عمل مؤشر جديد على العقد لمنع الألتباس و تجنبا للأخطاء 
        while current.left is not None :
            current = current.left
        return current.data

    def calculate_sum(self):
        total=0
        if self.left :
            total += self.left.calculate_sum()
        total += self.data
        if self.right :
            total += self.right.calculate_sum()
        return total

    def delete(self, val) :
        if val > self.data :
            if self.right != None :
                self.right = self.right.delete(val)
        elif val < self.data :
            if self.left != None :
                self.left = self.left.delete(val)
        else :
            if self.right is None and self.left is None :
                return None 
            elif self.left is None :
                return self.right 
            elif self.right is None :
                return self.right 
        if self.right is not None : # لأنه في الرجوع بالتكرار القيمه للفرع اليمين بتبقى None 
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def __str__(self): # print_tree BST in graph 
        ...

def build_BinaryTree(lis:list): # implement Binary_Tree From List of element
    mytree=Bst(lis[0])
    for i in lis[1:] :
        mytree.add_child(i)
    return mytree



# if __name__ == "__main__" :
#     x=[5,0,-5,-10,10,10,10,45,15,20,30,25]
#     mybt=build_BinaryTree(x)
    
#     print(x) # ترتيب النود حسب المدخل أولا
#     print(mybt.in_order()) # Travels DFS (in-order) Type
#     print("#" * 50)

#     print(mybt.search(10)) 
#     print(mybt.search(-20))
#     print(mybt.data)
#     print("#" * 50)

#     print(mybt.calculate_sum())
#     print("#" * 50)

#     print(mybt.right.right.left.find_max())
#     print(mybt.find_min())
#     print("#" * 50)

#     print(mybt.in_order())
#     print(mybt.post_order_traversal()) 
#     print(mybt.pre_order_traversal())
#     mybt.delete(10)
#     print(mybt.pre_order_traversal())
