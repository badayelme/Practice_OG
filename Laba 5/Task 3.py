import random
array = [random.randint(1,100) for i in range(100)]
array_2 = []
for i in array:
    if i % 2 == 0:
        array_2.append(i)
    else:
        array.remove(i)
array_2.sort()
print(array_2)