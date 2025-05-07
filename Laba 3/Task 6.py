import random
array = [random.randint(-10, 10) for i in range(10)]
def product_nums(array):  # 1 usage
    product = 1
    for i in range(len(array)):
        if i % 2 != 0:
            product *= array[i]
    return product
print(array)
print(f"Произведение чисел с нечетными местами: {product_nums(array)}")