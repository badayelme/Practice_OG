num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))

def numbers(num_1, num_2):
    if num_1 > num_2:
        print(f"Наибольшее: {num_1}")
    else:
        print(f"Наибольшее: {num_2}")

numbers(num_1, num_2)