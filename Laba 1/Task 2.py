list = [1,2,3,4,5,6]
def change(list):
    list[0], list[-1] = list[-1], list[0]
    return list
print(change(list))