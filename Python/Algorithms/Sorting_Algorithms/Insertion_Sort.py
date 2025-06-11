my_array = [64, 12, 34, 25, 12, 22, 11, 90, 5]

def Insertion_sort(arr:list): # the indian guy
    for i in range(1,len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > element :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = element
    print("Sorted array:", arr)
Insertion_sort(my_array)



def Insertion_sort(arr:list): # my implementation
    for i in range(1,len(arr)):
        insert_index = i
        element = arr.pop(i)
        for j in range(i-1,-1,-1):
            if element < arr[j] :
                insert_index = j
        arr.insert(insert_index, element)
    print("Sorted array:", arr)
Insertion_sort(my_array)



my_array = [64, 12, 34, 25, 12, 22, 11, 90, 5] # W3 School
n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)
print("Sorted array:", my_array)



my_array = [64, 12, 34, 25, 12, 22, 11, 90, 5] # W3 School Improvement
n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value
print("Sorted array:", my_array)
