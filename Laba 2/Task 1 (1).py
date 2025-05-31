import random

numbers = [random.randint(1, 100) for num in range(10)]

min_value = min(numbers)
min_index = numbers.index(min_value)
print(f"Коллекция: {numbers}")
print(f"мин. число: {min_value}")
print(f"индекс мин. числа: {min_index}")