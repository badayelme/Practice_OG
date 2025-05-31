num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

def max_nums(num1, num2):
    return max(num1, num2)

print(f"Максимальное число: {max_nums(num1, num2)}")