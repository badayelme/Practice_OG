import random
array = []
random_array = [random.randint(0,100) for i in range(15)]
for i in random_array:
    array.append(i)
print(array)
for i in array:
    print(i)