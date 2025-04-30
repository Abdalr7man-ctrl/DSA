import heapq # Its library to use heap in python
# print(heapq.__doc__)

def heapify(arr, n, i):

    # Iam access the index of the left and right Node of the parent to compere them
    left_node = i * 2 + 1
    right_node = i * 2 + 2

    largest = i

    if left_node < n and arr[left_node] > arr[largest]:
        largest = left_node

    # بقارن بالأندكس للمتغير الأكبر عشان يمكن يتغير من المقارنه الي فوق
    if right_node < n and arr[right_node] > arr[largest]:
        largest = right_node

    if i != largest: # يعني لو الأندكس بتاع النود مطعلش هو الأكبر وأتغير
        arr[largest], arr[i] = arr[i], arr[largest] # ببدله بالنود الأكبر منه
        
        # برجع أعمل تاني الداله عشان أتابع النود الي بدلتها أشوفها نزلت لمكان صح بالنسبه لها ولا هتحتاج تبديل تاني مع ولادها الجدد
        heapify(arr, n, largest)

def HeapSort(arr):

    n = len(arr)
    # Iam start from last Node None leaf
    # جبت الأندكس بتاع أخر نود ليها أبناء عن طريق اني جبت أندكس الأب لأخر عنصر الي هيكون أكيد أخر نود أب
    # مبدأش بأخر نود على طول و خلاص لأنهم كده كده معمولهم هيبي فاي مش لازملهم تبديل على زي النود الأب لو هعمل مين هيب او مكس 
    # و أخلي أكبر عنصر مكان النود الأب لو الماكس هيب
    for i in range((n // 2 - 1 ), -1, -1):
        heapify(arr, n, i)

    # at this point the arr will be heap tree Every node biger than his child and the root Node arr[0] is the bigest element

    for i in range(n-1, -1, -1):
        
        # هنا باخد أكبر عنصر من الأندكس زيرو و أحطه في أخر أندكس 
        arr[0], arr[i] = arr[i], arr[0] 

        # برجع تاني أعمل شجرة هيب بس على المصفوفه كلها معادا العناصر الأخيره الي مترتبه
        heapify(arr, i, 0)

arr = [9, 4, 3, 8, 10, 2, 5] 
HeapSort(arr)
print(arr)

# https://www.quora.com/What-are-the-benefits-of-heap-sort-and-its-disadvantages-compared-to-other-sorting-algorithms
# https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.geeksforgeeks.org/heap-sort/&ved=2ahUKEwi4q96hkueMAxUT8LsIHaTKIFsQFnoECAoQAQ&usg=AOvVaw2KQ-TMJrRDPlEf7-9SDbet
