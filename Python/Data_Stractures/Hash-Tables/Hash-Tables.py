# Implementation of Dict

def get_hash(key):
    h=0
    for char in key :
        h+=ord(char)  # h += ASCII value of char 
    return h % 100 # make Hash of Value(key) in Hash map

print(get_hash("Abdalrhman"))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [ [] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key :
            h+=ord(char)  # h += ASCII value of char 
        return h % self.MAX # make Hash of Value(key) in Hash map

    def __setitem__(self,key,val):
        self.arr[self.get_hash(key)]=val

    def __getitem__(self,key):
        return self.arr[self.get_hash(key)]

    def __delitem__(self,key):
        self.arr[self.get_hash(key)]=None

t=HashTable()

print(t.get_hash("Abdalrhman"))

t["Abdalrhman"]="10th 0f ramadan" # it was like that -->  t.add("Abdalrhman","10th 0f ramadan")

print(t.arr)

print(t["Abdalrhman"]) # it was like that --> t.get("Abdalrhman")

del t["Abdalrhman"]

print(t.arr)

print(ord("a"))

