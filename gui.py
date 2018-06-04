import time, sys, math
import numpy as np
from tkinter import *


def solver(first_arr, second_arr):
    a = np.array(first_arr)
    b = np.array(second_arr)
    x = np.linalg.solve(a, b)
    return x


def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0","end")
    output.insert("0.0",value)


def handler():
    """ Get the content of entries and passes result to the output area """
    inserter(solver(array, b_arr))


# родительский элемент
root = Tk()
# устанавливаем название окна
root.title("Решение СЛАУ методом Гаусса")
# устанавливаем минимальный размер окна
root.minsize(325, 230)
# выключаем возможность изменять окно
root.resizable(width=False, height=False)

# создаем рабочую область
frame = Frame(root)
frame.grid()
array = []
b_arr = []


# функция, обрабатывающая массив
def array_accept():

            global array, b_arr
            ar = [int(elem) for elem in x1m.get().split()]
            array.append(ar)
            array = list(array)
            if x2m.get() != '':
                ar = [int(elem) for elem in x2m.get().split()]
                array.append(ar)
                array = list(array)
            if x3m.get() != '':
                ar = [int(elem) for elem in x3m.get().split()]
                array.append(ar)
                array = list(array)
            if x4m.get() != '':
                ar = [int(elem) for elem in x4m.get().split()]
                array.append(ar)
                array = list(array)
            print(array)

            ar = int(b1m.get())
            b_arr.append(ar)
            if b2m.get() != '':
                ar = int(b2m.get())
                b_arr.append(ar)
            if b3m.get() != '':
                ar = int(b3m.get())
                b_arr.append(ar)
            if b4m.get() != '':
                ar = int(b4m.get())
                b_arr.append(ar)
            print(array, b_arr)

header = Label(frame, text="Введите данные").grid(row=1, column=3)

# поля для ввода массва a
x1m_lab = Label(frame, text="a1m").grid(row=2, column=1)
x1m = Entry(frame, width=10)
x1m.grid(row=2, column=2)
x2m_lab = Label(frame, text="a2m").grid(row=3, column=1)
x2m = Entry(frame, width=10)
x2m.grid(row=3, column=2)
x3m_lab = Label(frame, text="a3m").grid(row=4, column=1)
x3m = Entry(frame, width=10)
x3m.grid(row=4, column=2)
x4m_lab = Label(frame, text="a4m").grid(row=5, column=1)
x4m = Entry(frame, width=10)
x4m.grid(row=5, column=2)

# поля для ввода  b
b1m_lab = Label(frame, text="b1m").grid(row=2, column=3)
b1m = Entry(frame, width=5)
b1m.grid(row=2, column=4)
b2m_lab = Label(frame, text="b2m").grid(row=3, column=3)
b2m = Entry(frame, width=5)
b2m.grid(row=3, column=4)
b3m_lab = Label(frame, text="b3m").grid(row=4, column=3)
b3m = Entry(frame, width=5)
b3m.grid(row=4, column=4)
b4m_lab = Label(frame, text="b4m").grid(row=5, column=3)
b4m = Entry(frame, width=5)
b4m.grid(row=5, column=4)


# кнопка принять массив
but_accept1 = Button(frame, text="Accept", command=array_accept).grid(row=2, column=7, padx=(10,0))
# кнопка решить
but = Button(frame, text="Solve", command=handler).grid(row=3, column=7, padx=(10,0))
# место для вывода решения уравнения
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=12, columnspan=8)

# запускаем главное окно
root.mainloop()
