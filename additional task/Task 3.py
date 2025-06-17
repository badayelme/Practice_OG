class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
            self.__balance += amount
            return f"Депозит {amount}."

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Снято {amount}."
        else:
            return "Недостаточно средств для вывода."

    def get_balance(self):
        return self.__balance

deposit = int(input("Сколько денег на вашем счету: "))
account = BankAccount(deposit)

while True:
    choice = int(input("1 - Внести депозит\n2 - Снять со счёта\n3 - Показать баланс\n"))
    if choice == 1:
        deposit_plus = int(input("Сколько хотите внести: "))
        account.deposit(deposit_plus)
    elif choice == 2:
        deposit_minus = int(input("Сколько хотите снять: "))
        account.withdraw(deposit_minus)
    elif choice == 3:
        print("Ваш баланс:", account.get_balance())