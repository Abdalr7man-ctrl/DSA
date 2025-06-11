"""
The time complexity is : Big O(log(n))

its work on sorted array
"""

def Binary_Search(arr:list, target) -> int:

    middle = len(arr) // 2
    left = 0
    right = len(arr)

    while arr[middle] != target:

        if arr[middle] > target :
            right = middle
            middle = (left + right) // 2
        elif arr[middle] < target :
            left = middle + 1
            middle = (left + right) // 2
        if left >= right :
            return -1

    return middle

my_arr = [1, 2, 4, 5, 8, 11]
print(Binary_Search(my_arr, 1))
