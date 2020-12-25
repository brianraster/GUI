from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0,'Enter your Name: ')

# Function for what a click does
def myClick():
    hello = 'Hello '
    myLabel = Label(root, text= hello + e.get())
    myLabel.pack()


myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()
