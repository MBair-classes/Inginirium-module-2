from tkinter import *

def greet_user():
    username = name_field.get()
    label.config(text=f"Привет, {username}.")

root = Tk()
root.geometry("250x200")
label = Label(width = 30, height=2, bg = 'white', fg = 'black')
button = Button(width = 15, height=5, bg = 'green', fg = 'black', text="Приветствие", command=greet_user)
name_field = Entry(width = 15, bg = 'gray', fg = 'white')

label.pack()
button.pack()
name_field.pack()

root.mainloop()
