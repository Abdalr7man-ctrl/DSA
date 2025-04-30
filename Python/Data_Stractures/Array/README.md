```python
#--------(Arrays in python)-------------#
x=[2200,2350,2600,2130,2190]

print(sum(x))
print(sum(x[0:2]))

[print(True) if i == 2000 else i for i in x]

x.append(1980)

x=int(input("put number to make list from even number to this number: "))
print([ i for i in range(x) if i % 2 ==0 ])

x = int(input("put number to make list from odd number to this number: "))
odd_numbers = [i for i in range(x + 1) if i % 2 != 0]
print(odd_numbers)
```