"""
https://www.w3schools.com/dsa/dsa_algo_mergesort.php
Divide the unsorted array into two sub-arrays, half the size of the original.
Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
Merge two sub-arrays together by always putting the lowest value first.
Keep merging until there are no sub-arrays left.

The merge Sort Use the (Recursion, Divide & Conquer, Two pointers)
Merge Sort Implementation:
To implement the Merge Sort algorithm we need:
    1-An array with values that needs to be sorted.
    2-A function that takes an array, splits it in two, and calls itself with each half of that array
    so that the arrays are split again and again recursively, until a sub-array only consist of one value.
    3-Another function that merges the sub-arrays back together in a sorted way.
"""

# def Merge_Sort(arr):
#     if len(arr) <= 1 :
#         return arr
#     left = Merge_Sort(arr[:len(arr)//2])
#     right = Merge_Sort(arr[len(arr)//2:])
#     return Merge(left, right)

# def Merge(sub_left, sub_right):
#     result = []
#     i = j = 0
#     while len(sub_right) > i and len(sub_left) > j :
#         if sub_right[i] < sub_left[j] :
#             result.append(sub_right[i])
#             i += 1
#         else :
#             result.append(sub_left[j])
#             j += 1
#     result.extend(sub_right[i:])
#     result.extend(sub_left[j:])
#     return result

myarr = [3,2,1,-1]
# print(Merge_Sort(myarr))


# Merge Sort without Recursion

def Merge_Sort(arr):
    step = 1
    length = len(arr)

    while length > step :
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            
            merged = Merge(left, right)
            
            # Place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val
                
        step *= 2  # Double the sub-array length for the next iteration
        
    return arr

def Merge(l, r):
    resulte = []
    i = j = 0
    
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            resulte.append(l[i])
            i += 1
        else :
            resulte.append(r[j])
            j += 1    
    resulte.extend(r[j:])
    resulte.extend(l[i:])
    
    return resulte

print(Merge_Sort(myarr))
