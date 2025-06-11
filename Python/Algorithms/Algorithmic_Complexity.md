## Poiner Machine , RAM 


## O(1) : Give Big O(1) all the time (Constant Time) 

```python
 def O1(arr):
     print("Hello world")

 O1([1,2,3,4,5,6,7]) # Even if the array have huge number of the element
```


## O(n) : Give Big O(n) all the time (liner Time)

```python
def On(arr) :
    for i in arr :
        print("Hello World") # This Operation Have Big O(1) But It is repeated (n == len(arr)) Time

# On([1,2,3,4,5,6,7]) # --> Big O(n)
```


## O(n^2) : Give Big O(n^2) all the time (Quadratic Time)

```python
def On2(arr) :
    number = 1
    for i in arr :
        for j in arr :
            print(f"{number}-Hello World")
            number += 1

On2([1,2,3,4,5,6,7])
```


## O(n^3) : Give Big O(n^3) all the time (Cube Time)

```python
def On3(n):
    for i in range(n) :
        for j in range(n) :
            for k in range(n):
                print((i, j, k))

On3(2)
```

## O(log(n)) : Give Big O(log(n))

```python
def Olog(n) : # log2(n) == 2^? = n
    while n != 1 :
        print(n)
        n = n // 2
        return  Olog(n)

Olog(256) # --> log(256) = 8 
```

## O(nlog(n)) : Give Big O(nlog(n)) all the time (Logarithmic time)

```python
def Onlog(n) :
    y = n # To make the same loop each time i divide the n 
    while n > 1 :
        n = n // 2 
        for i in range(y): # the loop its occur log(n) time 
            print("Hello World") # This print occur n * log(n) time

Onlog(4)
```

## O(2^n) : Give Big O(2^n) all the time (Exponential time)

```python
def fib(n):
    if n < 2 :
        return 0
    return fib(n-1) + fib(n-2) # الداله هنا في كل مره بتتضاعف و تعمل دالتين قبينتج عنه التقعيد بينمو بشكل أسي بسبب التضاعف مع كل زياده

fib(4)
```

```python
# def all_subsets(arr):
#     """
#     تعيد قائمة بجميع الأجزاء (Subsets) لمصفوفة arr.
#     عدد الأجزاء الناتج هو 2^n حيث n = len(arr).
#     """
#     # إذا كانت المصفوفة فارغة، فالمجموعة الوحيدة هي الجزء الفارغ
#     if not arr:
#         return [[]]
    
#     # نفصل العنصر الأول عن بقية المصفوفة
#     first = arr[0]
#     rest = arr[1:]
    
#     # نحصل على جميع الأجزاء دون استخدام العنصر الأول
#     subsets_without_first = all_subsets(rest)
    
#     # نُنشئ أجزاءً جديدة بإضافة العنصر الأول إلى كل جزء في القائمة السابقة
#     subsets_with_first = []
#     for subset in subsets_without_first:
#         subsets_with_first.append([first] + subset)
    
#     # ندمج القائمتين: الأجزاء التي لا تحتوي على العنصر الأول والأجزاء التي تحتوي عليه
#     return subsets_without_first + subsets_with_first

# # تجربة على مصفوفة صغيرة
# example = [1, 2, 3]
# result = all_subsets(example)
# print("All subsets of", example, ":")
# for subset in result:
#     print(subset)
# print(result)
```

## O(n!) : Factorial.

```python
count = 1
def factorial(n):
    global count
    if n == 0 :
        print(count)
        count += 1
        return
    for i in range(n):
        factorial(n-1)

factorial(5)
```

#---------------------(Space Coplexity)---------------------#

def space(n):
    if n == 0:
        print("Hello")
        return 
    space(n-1)

space(3) # Its Make 3 Function Take Space in the stack memory

