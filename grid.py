from tkinter import *

root = Tk()

# Creating a label widget and
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Brian")
myLabel3 = Label(root, text="random string of text")

# packing it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=2, column=7)

root.mainloop()
