# Імпортуємо текстовий формат обміну данних JSON а також біліотеку tkinter
import json
import http.client
from tkinter import *
import tkinter as tk

# Створюємо загальний екран на якому буде показано наші дані

screen = Tk()
screen.title("Статистика COVID")
screen.geometry("600x750")
screen['bg'] = '#a1e3a3'

n = 6  # Кількість країн, які нам виведе програма

# Код взятий з сайту

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "870f102616msh0ed5dccee3ab615p199f57jsn744c73dbb482",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}

conn.request("GET", "/api/covid-ovid-data/sixmonth/USA", headers=headers)
res = conn.getresponse()
data = res.read()
inform = data.decode("utf-8")
json = json.loads(inform)


# Функція, яка буде оновлювати дані для країн

def update():
    import json
    text.delete(1.0, tk.END)
    conn.request("GET", "/api/covid-ovid-data/sixmonth/USA", headers=headers)
    res = conn.getresponse()
    data = res.read()
    inform = data.decode("utf-8")
    json = json.loads(inform)
    text.insert('1.0', '\n')
    text.insert('1.0', '-' * 40)
    for i in range(n):
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[1])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[2])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[3])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[4])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[5])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[6])
        text.insert('1.0', '-' * 50)


# Функція, яка буде перевіряти країну в форматі JSON і виводити результат

def static():
    k = 0
    for i in range(n):
        chooseCountry = entryCountry.get()
        getCountry = json[i].get('country')
        if chooseCountry == getCountry:
            text.insert('1.0', '\n')
            text.insert('1.0', json[i].get('total_cases'))
            text.insert('1.0', '\n')
            text.insert('1.0', json[i].get('total_deaths'))
            text.insert('1.0', '\n')
            text.insert('1.0', json[i].get('total_recovered'))
            text.insert('1.0', '\n')
            text.insert('1.0', json[i].get('country'))
            text.insert('1.0', '\ncountry')
            text.insert('1.0', '\nFOUND!')
        else:
            k += 1
        if k == 6:
            text.insert('1.0', '\n')
            text.insert('1.0', '\nDID`NT FOUND!')


# Поле пошуку, кнопка відображення статистики та кнопка оновлення відповідно. Вони виконують команди та посилаються на функції прописані вище

entryCountry = Entry(width=40, bg='#446945', fg='#fff')
entryCountry.insert(0, 'Введіть країну')
entryCountry.pack(side=TOP, pady=10)

staticButton = Button(text='Відобразити дані', height=3, width=20, command=static)
staticButton.pack(expand=1, side=BOTTOM, pady=5, padx=5)

updateBut = Button(text="Оновити", height=3, width=20, command=update)
updateBut.pack(expand=1, side=BOTTOM, pady=5, padx=5)

text = Text(width=70, height=100)
text.pack(side=TOP)

# Виклик функції оновлення, та виведення результату

update()
screen.mainloop()