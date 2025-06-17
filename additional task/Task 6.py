class Nikola:
    __slots__ = ['_name', '_age']

    def __init__(self, name, age):
        self._name = name if name == "Николай" else f"Я не {name}, а Николай"
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

person_1 = Nikola("Николай", 30)
print(f"Имя: {person_1.name}")
print(f"Возраст: {person_1.age}")

person_2 = Nikola("Олег", 25)
print(f"Имя: {person_2.name}")
print(f"Возраст: {person_2.age}")