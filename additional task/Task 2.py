class Animal:
    def speak(self):
        return

class Dog(Animal):
    def speak(self):
        return "ГООООЙДА!"

class Cat(Animal):
    def speak(self):
        return "МЯУ!"

dog = Dog()
cat = Cat()

print("Dog says:", dog.speak())
print("Cat says:", cat.speak())