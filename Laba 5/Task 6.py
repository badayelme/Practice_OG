array = [1,-2,3,6,1,-10,-4]
for i in range(len(array)):
    if array[i] > 0:
        array[i] = -array[i]
    else:
        array[i] = abs(array[i])
print(array)