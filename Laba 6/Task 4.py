numbers = [-1, -2, -3, 4, 5, -6, 7, -8, 9]
first_positive = 1
last_negative = 0

for num in numbers:
        if num > 0 and first_positive == 1:
            first_positive = num
        if num < 0:
            last_negative = num

print(f"Первый положительный элемент: {first_positive}")
print(f"Последний отрицательный элемент: {last_negative}")