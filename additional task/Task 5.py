class KgToPounds:
    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, value):
            self._kg = value

    def to_pounds(self):
        return self._kg * 2.20462

kg_user = int(input("Введите kg: "))
converter = KgToPounds(kg_user)

while True:
    choice = int(input("1 - Вывести\n2 - Перевести в фунты\n3 - Установить новое значение\n4 - Завершить\n"))
    if choice == 1:
        print(converter.kg)
    elif choice == 2:
        print(converter.to_pounds())
    elif choice == 3:
        kg_user_now = int(input("Введите новое kg: "))
        converter.kg = kg_user_now
        print(converter.kg)
    elif choice == 4:
        break