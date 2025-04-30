"""
Sudo Code :
1-Go through the array to find the lowest value.
2-Move the lowest value to the front of the unsorted part of the array.
3-Go through the array again as many times as there are values in the array.
"""

def selection_sort(arr:list):
    """Function for selection sort Algorithm"""
    for i in range(len(arr)-1):
        min_value = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > min_value: # arr[j] < min_value To Sort the array decreasing  (Descending)
                continue
            else :
                min_value = arr[j]
                min_index = j
        if i != min_index:
            arr.pop(min_index)
            arr.insert(i, min_value)
    return arr

def selection_sort(arr:list):
    """
    Sorting Algorithm More Customize By use Direct Switch 
    its Avoid the insert and pop(Shifting Problem) wich make O(n)
    """
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[min_index]: # arr[j] < min_value To Sort the arr from the Maximum 
                continue
            else :
                min_index = j
        if i != min_index:
            arr[min_index], arr[i] = arr[i], arr[min_index] # Direct Switch Without any continuer in the midel
    return arr

my_arr = [1,1,1.1,-2,-2,-1,0,1.1,12,1.1, 12,3,4,5,6,6]
print(selection_sort(my_arr))
print(my_arr)
