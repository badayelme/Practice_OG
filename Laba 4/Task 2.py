array = []
sum_element = 0
for i in range(14):
    element = int(input("Enter a number: "))
    sum_element = sum_element + element
    array.append(element)
array.append(sum_element)
print(array)
for i in array:
    print(i)