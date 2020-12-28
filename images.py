from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Working with images')
root.iconbitmap('dot.ico')

myImg = ImageTk.PhotoImage(Image.open('heart.png'))
label = Label(image=myImg)
label.pack()

quitButton = Button(root, text='Exit Program', command=root.quit)
quitButton.pack()

root.mainloop()
