array = []

while True:
    element = input("Enter the element: ")
    if element == '':
        break
    else:
        array.append(element)

longest = max(array, key=len)
shortest = min(array, key=len)

print(f"The longest item in the list: {longest}\nThe shortest item in the list: {shortest}")