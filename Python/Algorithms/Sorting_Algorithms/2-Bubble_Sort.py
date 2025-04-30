
def Bubble_sort(arr:list) -> str:
    n = len(arr)-1
    operations = 0
    for i in range(n):
        for j in range(n-i): # n-i --> عشان المقارنات تقل في كل لفه لأن في كل مره في عنصر بيوصل لمكانه الي هو أكبر عنصر في أول مره
            operations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return f"The Sorted array: {arr}\nThe number of operations: {operations}"

my_arr = [ i for i in range(1000)]
print(Bubble_sort(my_arr))

def Bubble_Sort(arr:list) -> str:
    """Its improve by add swape what will stop if the array is alerdy sorted"""
    n = len(arr)-1
    operations = 0
    for i in range(n):
        swape = False
        for j in range(n-i): # n-i --> عشان المقارنات تقل في كل لفه 
            operations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swape = True
        if swape is False:
            break
    return f"The Sorted array: {arr}\nThe number of operations: {operations}"

print(Bubble_Sort(my_arr))
