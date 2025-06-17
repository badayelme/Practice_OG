from datetime import datetime

def action_date(user_date):
    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    date = datetime.strptime(user_date, "%d.%m.%Y")

    day_of_week = days_of_week[date.weekday()]
    day = date.day
    month = months[date.month]
    year = date.year

    return f"{day_of_week}, {day} {month}, {year} year"

user_date = input("Enter date (day.month.year): ")
print(action_date(user_date))