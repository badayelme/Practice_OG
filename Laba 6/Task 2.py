class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

users = [
    User("user_1", "123123"),
    User("user_2", "321321"),
    User("user_3", "112233"),
    User("user_4", "131313"),
    User("user_5", "232323"),
]

def find_user(users):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in users:
        if user.login == login and user.password == password:
            return user

found_user = find_user(users)

if found_user:
    print(f"Пользователь найден: Логин - {found_user.login}, Пароль - {found_user.password}")
else:
    print("Пользователь не найден")