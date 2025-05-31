import random
array = [random.randint(-10, 10) for i in range(10)]
def positive(array):  # 1 usage
    number = 0
    for i in array:
        if i > 0:
            number += 1
    return number
print(array)
print(f"Количество положительных чисел: {positive(array)}")