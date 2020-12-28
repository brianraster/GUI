from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('dot.ico')

myImg1 = ImageTk.PhotoImage(Image.open("images/apple.png"))
myImg2 = ImageTk.PhotoImage(Image.open("images/banana.png"))
myImg3 = ImageTk.PhotoImage(Image.open("images/cherry.png"))
myImg4 = ImageTk.PhotoImage(Image.open("images/grapes.png"))
myImg5 = ImageTk.PhotoImage(Image.open("images/orange.png"))

imgList = [myImg1, myImg2, myImg3, myImg4, myImg5]

label = Label(image=myImg1)
label.grid(row=0, column=0, columnspan=3)

def forward(imageNum):
    global label
    global backButton
    global nextButton

    label.grid_forget()
    label = Label(image=imgList[imageNum-1])
    nextButton = Button(root, text=">>", command=lambda: forward(imageNum+1))
    backButton = Button(root, text="<<", command=lambda: back(imageNum-1))

    if imageNum == 5:
        nextButton = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    nextButton.grid(row=1, column=2)

def back(imageNum):
    global label
    global backButton
    global nextButton

    label.grid_forget()
    label = Label(image=imgList[imageNum-1])
    nextButton = Button(root, text=">>", command=lambda: forward(imageNum+1))
    backButton = Button(root, text="<<", command=lambda: back(imageNum-1))

    if imageNum == 1:
        backButton = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    nextButton.grid(row=1, column=2)

backButton = Button(root, text="<<", command=back, state=DISABLED)
exitButton = Button(root, text="EXIT", command=root.quit)
nextButton = Button(root, text=">>", command=lambda: forward(2))

backButton.grid(row=1, column=0)
exitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2)

root.mainloop()
