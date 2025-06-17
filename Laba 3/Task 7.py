number = int(input("Введите число: "))
def decreasing(number):  # 1 usage
    info_number = str(number)
    for i in range(len(info_number)):
        if int(info_number[i]) > int(info_number[i+1]):
            return "Числа расположены по убыванию"
        elif int(info_number[i]) < int(info_number[i+1]):
            return "Числа расположены не по убыванию"
        else:
            return "Числа повторяются"
print(decreasing(number))