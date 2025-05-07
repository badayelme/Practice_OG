width = int(input("Введите ширину прямоугольника: "))
length = int(input("Введите длину прямоугольника: "))
side_square = int(input("Введите сторону квадрата: "))

def number_of_squares():
    S_rectangle = width * length
    S_square = side_square * side_square
    squares = S_rectangle / S_square
    return squares

print(f"Количество квадратов: {number_of_squares()}")