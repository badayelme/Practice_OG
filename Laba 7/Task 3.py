array = [39,22,-3,4,53,-5,2,5,-10,4,81,2,-13,-2]
array_2 = []
for i in array:
    if i > 0 and 10 <= i <= 99:
        array_2.append(i)
array_2.sort()
print(array)
print(array_2)