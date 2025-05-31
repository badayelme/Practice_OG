array = [1,2,5,7,1,8,2,6,4,8,1,9,5,1,2,10,23,5,2]
def numbers(array):
    sum_num = 0
    composition_num = 1
    for i in array:
        if i > 0:
            sum_num += i
    index_max_num = array.index(max(array))
    index_min_num = array.index(min(array))

    start = min(index_max_num, index_min_num) + 1
    end = max(index_max_num, index_min_num)
    for i in range(start, end):
        composition_num *= array[i]
    print(f"Сумма чисел: {sum_num}, Произведение чисел: {composition_num}")
numbers(array)