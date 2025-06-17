array = []
spisok = [
    "kek",
    "yandex.ru",
    "http://lol",
    "http://invicible",
]

for i in range(len(spisok)):
    if spisok[i].startswith("http://"):
        array.append(spisok[i])
print(array)