from datetime import datetime
today_date = datetime.today()
day = today_date.strftime("%A")
month = today_date.strftime("%B")
print(f"{day}\n{month}\nOleg")