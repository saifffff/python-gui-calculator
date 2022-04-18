# imported all of the tkinter
from cProfile import label
import re
from struct import pack
from tkinter import *
# constructer
gui_root = Tk()

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

# sideBar = Frame(gui_root,bg="grey",borderwidth=5,relief=SUNKEN)
# sideBar.pack(side=LEFT,fill="y")

# sbtext = Label(sideBar, text="sidebar text")
# sbtext.pack()

# headBar = Frame(gui_root,bg="grey",borderwidth=5,relief=SUNKEN)
# headBar.pack(side=TOP,fill="x")

# hbtext = Label(headBar, text="Welcome to My Notepad",font="Helvetica 16 bold", fg ="red")
# hbtext.pack()

# >> buttons 

# >> button func
# def onclick():
#     print("thanks for the touch..")

# def onclickNot():
#     print("why the fuck would you do that..")

# frame = Frame(gui_root, borderwidth=6,bg="grey",relief=SUNKEN)
# frame.pack(side=LEFT,anchor="center")

# btn1 = Button(frame, fg="red",text="clickme",command=onclick)
# btn1.pack(side=LEFT,padx=10)

# btn2 = Button(frame, fg="red",text="Dont clickme",command=onclickNot)
# btn2.pack(side=LEFT,padx=10)

# btn3 = Button(frame, fg="red",text="ok clickme",command=onclick)
# btn3.pack(side=LEFT,padx=10)

# >> learning grid 
user = Label(gui_root, text="username")
password = Label(gui_root, text="password")
user.grid(row=1)
password.grid(row=2)

uval = StringVar()
pval = StringVar()

user_entry = Entry(gui_root, textvariable=uval)
pass_entry = Entry(gui_root, textvariable=pval)

user_entry.grid(row=1,column=2)
pass_entry.grid(row=2,column=2)

# shortcut to create a button

def getvals():
    print(f"Username = {uval.get()}")
    print(f"Password = {pval.get()}")

Button(text="Submit",command=getvals).grid()




# main event-Loop
gui_root.mainloop()


