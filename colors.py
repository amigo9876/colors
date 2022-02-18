from tkinter import *
import random
import time

root = Tk() # Переменная главного виджета или окна
# label - поле на котором располгается что либо
# Entry - это инпут куда можно вводить что либо

colors = ['red', 'green', 'blue', 'orange', 'black']

points = 0
text_task = "" # Рандомное задание
a1 = 6 # Эти переменные нужны на старте, чтобы программа не удаляла элементы внутри массива
a2 = 6 #

def random_task():
    global col, col_text, text_task
    col = ['red', 'green', 'blue', 'orange', 'black']
    col_text = ['red', 'green', 'blue', 'orange', 'black']
    text_task = colors[random.randint(0, len(colors) - 1)] # рандомное задание
    lab.config(bg=text_task) # Рандомное задание

    def random_color():
        if a2 < 5: # Если предыдущий результат уже получен
            col_text.pop(a2) #  удаляем этот вариант из массива
        num = random.randint(0, len(col) - 1)
        global a1
        a1 = num
        return num

    def random_text():
        if a1 < 5:
            col.pop(a1)
        num = random.randint(0, len(col_text) - 1)
        global a2
        a2 = num
        return num


    # Кнопки

    but.config(bg=col[random_color()], text=col_text[random_text()])
    but1.config(bg=col[random_color()], text=col_text[random_text()])
    but2.config(bg=col[random_color()], text=col_text[random_text()])
    but3.config(bg=col[random_color()], text=col_text[random_text()])
    but4.config(bg=col[random_color()], text=col_text[random_text()])

    def abs(): # муторная хуйня, чтобы по завершению формирования всех кнопок "обнулить" а2, чтобы в первой функции иф не сработал
        global a2
        a2 = 6
    abs()

    now = 0
    def update_clock():
        global now
        now = int(time.perf_counter())
        time_left.configure(text=now)
        root.after(1000, update_clock)

        if now > 5:
            time_left.configure(text='Время и стекло')
            result.configure(text=f'Ваш результат {points}')
            return

    update_clock()


def on_click(event):
    global text_task
    global points
    button_text = event.widget.cget('text') # получаем значение текстового поля нажимаемой кнопки
    if button_text == text_task: # сравниваем
        points += 1
        result.config(text=points)
    else:
        points -=1
        result.config(text=points)



# Визуал

# Задание и результат
lab = Label(root, text="Нужно выбирать кнопки с текстом, \nкоторые соответствуют цвету этого поля", bg="#fff", fg="black", width="40", height="10") # Внутри - параметры. 1 на каком виджете будет располагаться данный
result = Label(root, text="Очки", bg="#fff", fg="black", width="40", height="5")
time_left = Label(root, text="Clock", bg="#fff", fg="black", width="40", height="5")

#Кнопка старта
letsgo = but = Button(root, text="Поехали", bg="grey", fg="#fff", width='40', height="3", command=random_task)

#Кнопки клика
but = Button(root, text="Применять", bg="grey", fg="#fff", width='40', height="3", command=random_task)
but1 = Button(root, text="Применять", bg="grey", fg="#fff", width='40', height="3", command=random_task)
but2 = Button(root, text="Применять", bg="grey", fg="#fff", width='40', height="3", command=random_task)
but3 = Button(root, text="Применять", bg="grey", fg="#fff", width='40', height="3", command=random_task)
but4 = Button(root, text="Применять", bg="grey", fg="#fff", width='40', height="3", command=random_task)

but.bind('<Button-1>', on_click) # Событие по левому щелчку
but1.bind('<Button-1>', on_click)
but2.bind('<Button-1>', on_click)
but3.bind('<Button-1>', on_click)
but4.bind('<Button-1>', on_click)

lab.pack() # pack - располагает элемент на главном виджете
letsgo.pack()
but.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
time_left.pack()
result.pack()

root.mainloop() # Запуск программы
