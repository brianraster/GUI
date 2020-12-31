from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Using Frames')
root.iconbitmap('images/dot.ico')

frame = LabelFrame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

button = Button(frame, text='Click here')
button2 = Button(frame, text='...or here')
button.grid(row=0, column=0)
button2.grid(row=1, column=1)

root.mainloop()
