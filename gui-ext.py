import time, sys, math
import numpy as np
from tkinter import *


def solver(first_arr, second_arr):
    a = np.array(first_arr)
    b = np.array(second_arr)
    x = np.linalg.solve(a, b)
    return x

array=[]
entr_arr=[]
entr_arr_2=[]
y={"x%d"%a:None for a in range(1,11)}
x={"x%d"%a:None for a in range(1,11)}


def array_add():
    try:
        global n_val
        n_val = int(n.get())
        # поле для ввода массива
        for i in range(1, n_val + 1):
            global x, entr_arr
            x[i] = Entry(frame, width=8)
            x[i].grid(row=i+1, column=1)
            entr_arr.append(x[i])
           # print(x[i])
        print(entr_arr)
        for i in range(1, n_val + 1):
            global y, entr_arr_2
            y[i] = Entry(frame, width=2)
            y[i].grid(row=i+1, column=3)
            entr_arr_2.append(y[i])


    except:
        output.insert("1.0", "что-то пошло не так")
    return entr_arr

arr = []
def array_accept():

        for i in range(1, n_val+1):
            global array
            ar = [int(elem) for elem in x[i].get().split()]
            array.append(ar)
            array = list(array)
        print('a = ', array)
        for i in range(1, n_val+1):
            global arr
            ar = [int(elem) for elem in y[i].get().split()]
            arr.append(ar)
            arr = list(arr)
        print("b = ", arr)


def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0","end")
    output.insert("0.0",value)


def handler():
    """ Get the content of entries and passes result to the output area """
    n_val = int(n.get())
    inserter(solver(array, arr))


# родительский элемент
root = Tk()
# устанавливаем название окна
root.title("Решение СЛАУ")
# устанавливаем минимальный размер окна
root.minsize(325, 230)
# выключаем возможность изменять окно
root.resizable(width=False, height=False)

# создаем рабочую область
frame = Frame(root)
frame.grid()

# текст
n_lab = Label(frame, text="кол-во строк").grid(row=1,column=1)

# поле для ввода количества строк
n = Entry(frame, width=3)
n.grid(row=1, column=3)

# кнопка добавить массив
but_add = Button(frame, text="Add an array", command=array_add).grid(row=1, column=7, padx=(10,0))
# кнопка принять массив
but_add1 = Button(frame, text="Accept an array", command=array_accept).grid(row=2, column=7, padx=(10,0))
# кнопка решить
but = Button(frame, text="Solve", command=handler).grid(row=3, column=7, padx=(10,0))
# место для вывода решения уравнения
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=12, columnspan=8)

# запускаем главное окно
root.mainloop()