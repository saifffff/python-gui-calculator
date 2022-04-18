# imported all of the tkinter
from cProfile import label
import re
from tkinter import *
# constructer
gui_root = Tk();

# geometry is used to define width and height in same order widthxheight
gui_root.geometry("400x400")
# to define minnimun size
# min size takes args as width,height
gui_root.minsize(300,300)
# to define maximun size
# max size takes args as width,height
gui_root.maxsize(500,500)

# >> titles
gui_root.title("Python CALC by Saif Khan")

# >> title label
# title_label = Label(text ="Hello.. I am learning Tkinter :)",bg="red",fg="black",font=("comicsansms",10,"bold"),borderwidth=3, relief=SUNKEN    )
# title_label.pack()


# >>  working with labels
# myLabel = Label(text="this is my first label")
# myLabel.pack()

# >> working with images
# myPic = PhotoImage(file="img.png")
# myPicLabel = Label(image=myPic);
# myPicLabel.pack()

sideBar = Frame(gui_root,bg="grey",borderwidth=5,relief=SUNKEN)
sideBar.pack(side=LEFT,fill="y")

sbtext = Label(sideBar, text="sidebar text")
sbtext.pack()

headBar = Frame(gui_root,bg="grey",borderwidth=5,relief=SUNKEN)
headBar.pack(side=TOP,fill="x")

hbtext = Label(headBar, text="Welcome to My Notepad")
hbtext.pack()



#   --->  gui design
# main event-Loop
gui_root.mainloop()



