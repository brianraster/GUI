from tkinter import *

root = Tk()

# Function for what a click does
def myClick():
    myLabel = Label(root, text='Look! I clicked a button!')
    myLabel.pack()


myButton = Button(root, text="Click me", command=myClick)
myButton.pack()

root.mainloop()
