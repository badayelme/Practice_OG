import random
array = [random.randint(1, 100) for i in range(20)]
number_x = int(input("Введите число x: "))
print(array)

for i in array:
    if i == number_x:
        print("Число есть в массиве")
        break
else:
    print("Числа нет в массиве")