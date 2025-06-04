
class HashTable:
    """Implementation of the Hash Table"""
    def __init__(self):
        self.MAX = 100
        self.arr = [ [] for i in range(self.MAX)] # its represent the memory

    def get_hash(self, key):
        h = 0
        for char in key :
            h += ord(char)  # h += ASCII value of char
        return h % self.MAX # make Hash of Value(key) in Hash map

    def __setitem__(self, key, val): # object[name_key] = value
        self.arr[self.get_hash(key)] = val

    def __getitem__(self, key): # to get value of dictionary by use name of key
        return self.arr[self.get_hash(key)]

    def __delitem__(self, key): # to use del
        self.arr[self.get_hash(key)] = []

myDictionary = HashTable()

print(myDictionary.get_hash("Abdalrhman")) # return 2

# will add the the value at the index 2 according to the hash value
myDictionary["Abdalrhman"] = "10th 0f ramadan"

print(myDictionary.arr)

print(f"The value of the key: {myDictionary['Abdalrhman']}")

del myDictionary["Abdalrhman"]

# print(myDictionary.arr)
