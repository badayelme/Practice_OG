class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Итог: Газировка и {self.additive}")
        else:
            print("Итог: Обычная газировка")

limonad_choice = input("Введите добавку(Если нет, оставьте пустым): ")
if limonad_choice == '':
    limonad = Soda()
    limonad.show_my_drink()
else:
    limonad = Soda(limonad_choice)
    limonad.show_my_drink()