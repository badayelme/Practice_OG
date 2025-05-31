import random
length = random.randint(1, 25)
array = []
number = 3 * length
for i in range(length):
    array.append(number)
    number -= 3
print(f"Сгенерированный массив: {array}")