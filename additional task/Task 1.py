class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car = Car("Dodge", "RAM", 2020)

print("Марка:", car.make)
print("Модель:", car.model)
print("Год выпуска:", car.year)