from tkinter import *
from random import randint

def next_f():
    canvas.delete("all")
    option = randint(0, 2)
    if option == 0:
        f_args = [randint(1, 500) for i in range(4)]
        canvas.create_rectangle(f_args[0], f_args[1], f_args[2], f_args[3])
    elif option == 1:
        f_args = [randint(1, 500) for i in range(4)]
        canvas.create_oval(f_args[0], f_args[1], f_args[2], f_args[3])
    elif option == 2:
        f_args = [randint(1, 500) for i in range(6)]
        canvas.create_polygon(f_args[0], f_args[1], f_args[2], f_args[3], f_args[4], f_args[5])

root=Tk()
window_size = 550
root.geometry(f"{window_size}x{window_size}")

canvas = Canvas(root, width=500, height=500, bg='white')
canvas.pack()
Button(root, text='Новая фигура', width=15, height=2, bg='white', command=next_f).pack()

root.mainloop()