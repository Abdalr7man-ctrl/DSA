# https://algs4.cs.princeton.edu/34hash/
# https://realpython.com/python-hash-table/

class HashTable:
    """Implementation of the Hash Table"""
    def __init__(self):
        self.max = 100
        self.arr = [ [] for i in range(self.max)] # its represent the memory

    def get_hash(self, key):
        """Make Hash of the key by division"""
        hashing = 0
        for char in key :
            hashing += ord(char)  # h += ASCII value of char
        return hashing % self.max

    def __setitem__(self, key, val):
        """object[name_key] = value"""
        if val != self.arr[self.get_hash(key)]:
            self.arr[self.get_hash(key)].append(val)
            return
        self.arr[self.get_hash(key)].append(val)

    def __getitem__(self, key):
        """to get value of dictionary by use name of key"""
        return self.arr[self.get_hash(key)]

    def __delitem__(self, key):
        """to use del"""
        self.arr[self.get_hash(key)] = []

myDictionary = HashTable()

print(myDictionary.get_hash("Abdalrhman")) # return 2

# will add the the value at the index 2 according to the hash value
myDictionary["Abdalrhman"] = "10th 0f ramadan"
myDictionary["namhrladbA"] = "None" # the same hash of Abdalrhman == same index

print(myDictionary.arr)

print(f"The value of the key: {myDictionary['Abdalrhman']}")

del myDictionary["Abdalrhman"]

# print(myDictionary.arr)
