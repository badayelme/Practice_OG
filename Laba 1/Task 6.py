def season_events(number_of_month):  # 1 usage
    if number_of_month in [12,1,2]:
        events = "За окном падал белый снег"
    elif number_of_month in [3,4,5]:
        events = "Птицы пели прекрасные песни"
    elif number_of_month in [6,7,8]:
        events = "Солнце светило ярче чем когда-либо"
    elif number_of_month in [9,10,11]:
        events = "Урожай был невероятным"
    return print(f"Вы родились в {season[number_of_month-1]}. {events}.")

season = ["Январе", "Феврале", "Марта", "Апреле", "Мае", "Июне", "Июле", "Августе", "Сентябре", "Октябре", "Ноябре", "Декабре"]

try:
    number_of_month = int(input("Введите номер месяца в котором вы родились?: "))
except ValueError:
    print("Ошибка! Введите число")

season_events(number_of_month)