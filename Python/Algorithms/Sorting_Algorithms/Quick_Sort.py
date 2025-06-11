
def Quick_Sort(arr):
    """
    Not in place its make new array (Take space from the memory)
    """
    if len(arr) <= 1 :
        return arr
    pivot = arr.pop(len(arr)//2) # أهم حاجه ان المحور ميكونش موجود في المقارنه الي تحت
    left = [ i for i in arr if i < pivot ] # أصغر بس عشان لو ضيفت يساوي فكده هضيف العنصر مرتين مره هنا و مره في اليمين
    right = [ i for i in arr if i >= pivot]
    return Quick_Sort(left) + [pivot] + Quick_Sort(right)

arr = [8, 4, 7, 3, 5, 1, 2, 6, 6, 0, -1, 1.1]
sorted_arr = Quick_Sort(arr)
# print(sorted_arr)

#----------------------------------------------------------------------------#

def partition(array, low, high) -> int:
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1 # بزود واحد عشان هستعمله همؤشر للمكان الي هحطه فيه يكون وراه العناصر الي أصغر منه
            array[i], array[j] = array[j], array[i] # بقعد أجيب العنصر الصغير في الأول او عالشمال بالمعنى الأصح
    array[i+1], array[high] = array[high], array[i+1] # في الأخر بعد اللوب ببدل المحور مع عنصر من العناصر الي هتبقى على يمينه فبزود عليه واحد
    return i+1 # الأندكس للمكان الجديد

def Quick_Sort(array, low=0, high=None) -> None:
    """
    in place save the memory
    """
    if high is None:
        high = len(array) - 1
    
    if low < high:
        piovet_index = partition(array, low, high)
        Quick_Sort(array, low, piovet_index-1)
        Quick_Sort(array, piovet_index+1, high)

myarr = [3,2,1,0]
Quick_Sort(myarr)
print(myarr)
