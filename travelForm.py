from cProfile import label
from platform import java_ver

from tkinter import *

#  objective of this form is to understand grid layout 
#  how to work with entery widgets

# constructor
root = Tk()

# geometry wxh
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(400,400)

root.title("Travel Form Using Tkinter by Saif Khan")
# head label
Label(root, text="Welcome to Roads & Trails", font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

fullName = Label(root,text="Name")
address = Label(root,text="Address")
phone = Label(root,text="Phone")
gender = Label(root,text="Gender")
pmode = Label(root,text="Payment Mode")
econtact = Label(root,text="Emergency Contact")

fullName.grid(row=1,column=2)
address.grid(row=2,column=2)
phone.grid(row=3,column=2)
gender.grid(row=4,column=2)
pmode.grid(row=5,column=2)
econtact.grid(row=6,column=2)

#variable classes 

fullNameVal = StringVar()
addressVal = StringVar()
phoneVal = StringVar()
genderVal = StringVar()
pmodeVal = StringVar()
econtactVal = StringVar()
foodServiceVal = BooleanVar()


fullNameentry = Entry(root, textvariable=fullNameVal)
addressentry = Entry(root, textvariable=addressVal)
phoneentry = Entry(root, textvariable=phoneVal)
genderentry = Entry(root, textvariable=genderVal)
pmodeentry = Entry(root, textvariable=pmodeVal)
econtactentry = Entry(root, textvariable=econtactVal)

fullNameentry.grid(row=1,column=3)
addressentry.grid(row=2,column=3)
phoneentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
pmodeentry.grid(row=5,column=3)
econtactentry.grid(row=6,column=3)


# >> checkbox 
foodservice = Checkbutton(text="Include Meals",variable=foodServiceVal)
#packing checkbox
foodservice.grid(row=7,column=3)

# >> button design and logic
def onSubmit():
    print(f"Full Name = {fullNameVal.get()}")
    print(f"Address = {addressVal.get()}")
    print(f"Phone = {phoneVal.get()}")
    print(f"Gender = {genderVal.get()}")
    print(f"Payment Mode = {pmodeVal.get()}")
    print(f"Emergency Contact = {econtactVal.get()}")
    print(f"Include Meal = {foodServiceVal.get()}")
    

Button(text="Submit",command=onSubmit).grid(column=3)




# main event loop
root.mainloop()