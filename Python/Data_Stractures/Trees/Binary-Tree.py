# Resources: https://www.w3schools.com/dsa/dsa_data_binarytrees.php
# Resources: https://youtu.be/4r_XR9fUPhQ?si=PBsRjix_Z9kVHgMM

# # Resources for tree :
# https://www.geeksforgeeks.org/tree-data-structure/
# https://www.geeksforgeeks.org/introduction-to-tree-data-structure/

#---------------------(General Tree)---------------------#

class Tree:
    def __init__(self, data):
        self.data = data 
        self.children = []
        self.parent = None 

    def add_child(self, data):
        child = Tree(data)
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        prefix = self.level()*"  " + "|__" 
        print(prefix+self.data) if self.parent else print(self.data)
        for node in self.children :
            if node.data :
                node.print_tree()
        return ...

    def level(self):
        result = 0
        while self.parent != None :
            result += 1
            self = self.parent
        return result

root = Tree("Elctronic")
root.add_child("Laptop")
root.add_child("phone")
root.add_child("Tv")

root.children[0].add_child("Lenovo")
root.children[0].add_child("Asus")
root.children[0].add_child("msi")

root.children[1].add_child("Samasung")
root.children[1].children[0].add_child("S10")
root.children[1].children[0].add_child("M52")

root.children[1].add_child("Iphone")

# root.print_tree()

#---------------------(Binary Tree)---------------------#

class BinaryTree :
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        
        self.numleft = 0
        self.numright = 0

    def add_child(self, data):
        child = BinaryTree(data)
        
        child.parent = self
        
        if self.left is None:
            self.left = child
            self.numleft += 1
            return
    
        elif self.right is None:
            self.right = child
            self.numright += 1
            return

        if self.numleft == self.numright or self.numleft % 2 == 0:
            self.left.add_child(data)
            self.numleft += 1
            return
        
        elif self.numleft == self.numright + 2 or self.numleft % 2 != 0:
            self.right.add_child(data)
            self.numright += 1
            return

    def del_node(self, data):
        pass

    def __str__(self):
        return self.data

root = BinaryTree("A")

root.add_child("B")
root.add_child("C")
root.add_child("D")
root.add_child("E")
root.add_child("F")
root.add_child("G")
root.add_child("H")
root.add_child("I")

print(f"The Root: {root}")

print(f"The left Node: {root.left}")
print(f"The Right Node: {root.right}")

print(f"The left left Node: {root.left.left}")
print(f"The left right Node: {root.left.right}")

print(f"The right left: {root.right.left}")
print(f"The right right: {root.right.right}")

print(f"The left left left Node: {root.left.left.left}")
print(f"The left left right Node: {root.left.left.right}")
