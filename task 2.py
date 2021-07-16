# Підключаємо графічну та математичну бібліотеки

import tkinter
import math


# Функції, які відповідають за введення та виконання стандартних операцій

def add_digit(digit):
    value = count.get()
    if value[0] == '0':
        value = value[1:]
    count.delete(0, tkinter.END)
    count.insert(0, value + digit)


def add_oper(oper):
    value = count.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    count.delete(0, tkinter.END)
    count.insert(0, value + oper)


# Функція, яка реалізує виведення результату

def result():
    value = count.get()
    if value[-1] in '-+/*':
        value += value[:-1]
    count.delete(0, tkinter.END)
    count.insert(0, eval(value))


# Функція, очищає рядок введення

def clear():
    count.delete(0, tkinter.END)
    count.insert(0, 0)


# Нижче описані фeнкції, які використовують бібліотеку math для обчислення

def sin():
    value = count.get()
    x = float(value)
    value = math.sin(x)
    count.delete(0, tkinter.END)
    count.insert(0, value)


def cos():
    value = count.get()
    x = float(value)
    value = math.cos(x)
    count.delete(0, tkinter.END)
    count.insert(0, value)


def tg():
    value = count.get()
    x = float(value)
    value = math.tan(x)
    count.delete(0, tkinter.END)
    count.insert(0, value)


def ctg():
    value = count.get()
    x = float(value)
    value = math.ctg(x)
    count.delete(0, tkinter.END)
    count.insert(0, value)


def log():
    value = count.get()
    x = float(value)
    value = math.log5(x)
    count.delete(0, tkinter.END)
    count.insert(0, value)


def ln():
    value = count.get()
    x = float(value)
    value = math.log10(x)
    count.delete(0, tkinter.END)
    count.insert(0, value)


def per():
    value = count.get()
    x = float(value)
    if x > 0:
        value = x / 100
    count.delete(0, tkinter.END)
    count.insert(0, value)


def scr():
    value = count.get()
    x = float(value)
    if x > 0:
        value = math.sqrt(x)
    count.delete(0, tkinter.END)
    count.insert(0, value)


# Набір функцій з дизайном та функціоналом для кнопок

def button_number(digit):
    return tkinter.Button(text=digit, width=4, font=('Columbia', 18), bd=5, command=lambda: add_digit(digit))


def button_oper(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=lambda: add_oper(oper))


def button_count(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=result)


def button_clear(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=clear)


def button_sin(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=sin)


def button_cos(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=cos)


def button_tg(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=tg)


def button_ctg(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=ctg)


def button_log(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=log)


def button_ln(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=ln)


def button_per(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=per)


def button_scr(oper):
    return tkinter.Button(text=oper, width=4, font=('Columbia', 15), bg='#ebb0a4',
                          bd=5, command=scr)


# Встановлюємо розмір, колір, назву вікна

screen = tkinter.Tk()
screen['bg'] = '#b3e6b9'
screen.title('My calculator')
screen.geometry('480x300')

# Створюємо вікно калькулятора

count = tkinter.Entry(screen, justify=tkinter.RIGHT, font=('Columbia', 15), bg='#000', fg='white', width=18)
count.insert(0, '0')
count.grid(row=0, column=0, columnspan=6, stick='we', padx=5, pady=5)

# Викликаємо функції при введенні цифр

button_number('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
button_number('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
button_number('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
button_number('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
button_number('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
button_number('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
button_number('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
button_number('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
button_number('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
button_number('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

# Викликаємо функції при виборі дії(+, -, *, /)

button_oper('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
button_oper('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
button_oper('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
button_oper('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

# Викликаємо функції при виборі дії( обчислити, стерти)

button_count('=').grid(row=4, column=1, stick='wens', padx=5, pady=5)
button_clear('C').grid(row=4, column=2, stick='wens', padx=5, pady=5)

# Викликаємо функції при виборі тригонометричний чи інших складних дій

button_sin('sin').grid(row=1, column=4, stick='wens', padx=5, pady=5)
button_cos('cos').grid(row=2, column=4, stick='wens', padx=5, pady=5)
button_tg('tg').grid(row=3, column=4, stick='wens', padx=5, pady=5)
button_ctg('ctg').grid(row=4, column=4, stick='wens', padx=5, pady=5)
button_log('log').grid(row=1, column=5, stick='wens', padx=5, pady=5)
button_ln('ln').grid(row=2, column=5, stick='wens', padx=5, pady=5)
button_per('%').grid(row=3, column=5, stick='wens', padx=5, pady=5)
button_scr('sqrt').grid(row=4, column=5, stick='wens', padx=5, pady=5)

# Встановлюємо розміри для кнопок в колонці

screen.grid_columnconfigure(0, minsize=50)
screen.grid_columnconfigure(1, minsize=50)
screen.grid_columnconfigure(2, minsize=50)

# Встановлюємо розміри для кнопок в рядку

screen.grid_rowconfigure(1, minsize=60)
screen.grid_rowconfigure(2, minsize=60)
screen.grid_rowconfigure(3, minsize=60)
screen.grid_rowconfigure(4, minsize=60)

# Закінчення виконання команд

screen.mainloop()