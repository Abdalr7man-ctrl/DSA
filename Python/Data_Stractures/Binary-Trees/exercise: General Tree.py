# class Tree:
#     def __init__(self, name:str,  designation:str):
#         self. designation =  designation
#         self.name = name 
#         self.children = []
#         self.parent = None 

#     def add_child(self, name,  designation):
#         child = Tree(name,  designation)
#         child.parent = self
#         self.children.append(child)

#     def print_tree(self, hierarchy:str):

#         if hierarchy == "name" :
#             prefix = self.level()*"  " + "|__" 
#             print(prefix+self.name) if self.parent else print(self.name)
#             for node in self.children :
#                 if node.name :
#                     node.print_tree("name")
        
#         elif hierarchy == "designation" :
#             prefix = self.level()*"  " + "|__" 
#             print(prefix+self.designation) if self.parent else print(self.designation)
#             for node in self.children :
#                 if node.designation :
#                     node.print_tree("designation")

#         elif hierarchy == "both" :
#             prefix = self.level()*"  " + "|__" 
#             print(prefix+self.name+f"({self.designation})") if self.parent else print(self.name+f"({self.designation})")
#             for node in self.children :
#                 if node.designation :
#                     node.print_tree("both")

#         else : 
#             raise NameError("You should write (both or designation or name) as a string")

#     def level(self):
#         result = 0
#         while self.parent != None :
#             result += 1
#             self = self.parent
#         return result

# def build_management_tree(): # TODO : Make json file to take name and designation and use both to make Tree 
#     root = Tree("Nilupul", "CEO")
#     root.add_child("chinmay", "CTO")
#     root.add_child("Gels", "HR Head")
#     root.children[0].add_child("Vishwa", "Infrastructure Head")
#     root.children[0].add_child("Aamir", "Application Head")
#     root.children[0].children[0].add_child("Dhaval", "Cloud Manager")
#     root.children[0].children[0].add_child("Abhijit", "App Manager")
#     root.children[1].add_child("peter", "Recruitment Manager")
#     root.children[1].add_child("waqas", "policy Manager")
#     return root

# if __name__ == '__main__':
#     root = build_management_tree()
#     root.print_tree("name") # prints only name hierarchy
#     print("*" * 60)
#     root.print_tree("designation") # prints only designation hierarchy
#     print("*" * 60)
#     root.print_tree("both") # prints both (name and designation) hierarchy



#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################



# class Tree:
#     def __init__(self, data):
#         self.data = data 
#         self.children = []
#         self.parent = None 

#     def add_child(self, data):
#         child = Tree(data)
#         child.parent = self
#         self.children.append(child)

#     def print_tree(self, level):
#         if level > 0 :
#             prefix = self.level()*"  " + "|__" 
#             print(prefix+self.data) if self.parent else print(self.data)
#             level -= 1
#             for node in self.children :
#                 if node.data and level > 0 :
#                     node.print_tree(level)
    
#     def level(self):
#         result = 0
#         while self.parent != None :
#             result += 1
#             self = self.parent
#         return result



# if __name__ == "__main__" :
#     def bulid_location_tree():
#         root = Tree("Global")
#         root.add_child("Egypt")
#         root.add_child("Sudia")
#         root.children[0].add_child("Cairo")
#         root.children[0].add_child("Alxandria")
#         root.children[0].add_child("Aswan")
#         root.children[1].add_child("Almadina")
#         root.children[1].add_child("Maka")
#         root.children[1].add_child("Ryad")
#         root.print_tree(3)
#         print("*"*50)
#         root.print_tree(3)
#         print("*"*50)
#         root.print_tree(3)
#     bulid_location_tree()
