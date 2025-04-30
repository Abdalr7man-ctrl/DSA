"""
Sequential Search
OR
Liner Search
"""

def Liner_Search(arr, item):
    """liner Search with Big O(n)"""
    for i in arr:
        if i == item:
            return True
    return False

def Liner_Search(arr, item):
    """liner Search with While loop"""
    n = 0
    while n < len(arr):
        if arr[n] == item:
            return True
        else :
            n += 1
    return False

def Liner_Search(arr, item):
    """Delet this operation while n < len(arr):"""
    n = 0
    lenght = len(arr) # to keep the original lenght
    arr.append(item)
    while True:
        if arr[n] == item:
            if n == lenght: # if the loop out of the original array
                return False
            else:
                return True
        n += 1

my_arr = [i for i in range(1000)]
# print(Liner_Search(my_arr, 100))
# print(Liner_Search(my_arr, 10000000))


# The Alogorithm: Transpose Method

# Rule 20/80 : The data i searsh about it its reprecent the 20% of the data while me search is 80%.

# Self Organized Search : The most common item i search about it i put it in the first of the array.

# I should to use swap (a, b = b, a) or insert with linked list to avoid the shifting

# I use Self Organized Search When there item more search about it

# self organized search --> (Transpose, Move to front)

import time

def Transpose(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            if i//2 > 0 :
                arr[i], arr[i//2] = arr[i//2], arr[i]
            elif i > 0 :
                arr[i], arr[i-1] = arr[i-1], arr[i]
            return True
    return False

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")

start = time.time()
print(Transpose(my_arr, 1000))
end_time = time.time()
print(f"The time is : {end_time - start}")
