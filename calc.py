from tkinter import *
import math

# text variables
ansValGlobal = ""
finalValGlobal = ""


# init gui with tk class
gui = Tk()

# for title
gui.title('Calculator by Saif Khan')

# for icons
p1 = PhotoImage(file='shiats.png')
gui.iconphoto(False,p1)

# answer variable
Ans_val = StringVar()

# entry widget 1
Entry(gui, font=('futura', 25, 'bold'),
textvariable = Ans_val,
justify = LEFT).grid(columnspan=4, ipadx=120)

answerFinalLabel = StringVar()

# Entry widget 2
Entry(gui, font=('futura', 25, 'bold'),
textvariable = answerFinalLabel,
justify = LEFT).grid(columnspan = 4 , ipadx=120)


def changeAns_val(entry):
    global ansValGlobal
    global finalValGlobal 
    ansValGlobal = ansValGlobal + str(entry)
    finalValGlobal = ansValGlobal
    Ans_val.set(ansValGlobal)


def clearAns_val():
    global ansValGlobal
    global finalValGlobal
    finalValGlobal = ansValGlobal
    ansValGlobal = ""
    Ans_val.set(ansValGlobal)



def evaluateSquaregui():
    global ansValGlobal
    global finalValGlobal
    try:
        sqrtAnswer = math.sqrt(eval(str(finalValGlobal)))
        clearAns_val()
        answerFinalLabel.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(ansValGlobal)))
            clearAns_val()
            answerFinalLabel.set(sqrtAnswer)
        except(ValueError,SyntaxError,TypeError,ZeroDivisionError):
            clearAns_val()
            answerFinalLabel.set("Error!")


def evaluateAnswer():
    global ansValGlobal
    try:
       eval(ansValGlobal)
       evaluatedValueAnswerLabelGlobal= str(eval(ansValGlobal))
       clearAns_val()
       answerFinalLabel.set(evaluatedValueAnswerLabelGlobal)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearAns_val()
        answerFinalLabel.set("Error!")



def allClear():
    global ansValGlobal
    global finalValGlobal
    ansValGlobal = ""
    finalValGlobal = ""
    Ans_val.set("")
    answerFinalLabel.set("")



def createButton(txt,x,y):
    Button(gui, font=('futura', 15, 'bold'),
           padx=16,pady=16,text = str(txt),
           command = lambda:changeAns_val(txt),
           height = 2, width=9).grid(row = x , column = y, sticky=E)


buttons = ['AC','√','%','/','7','8','9','*','4','5','6','-','1','2','3','+','','','.','']
buttonsListTraversalCounter = 0

for i in range(3,8):
    for j in range(0,4):
        createButton(buttons[buttonsListTraversalCounter],i,j)
        buttonsListTraversalCounter =buttonsListTraversalCounter + 1

Button(gui,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "√",
       command = lambda:evaluateSquaregui(),
       height=2, width=9).grid(row = 3 , column = 1, sticky = E)



Button(gui,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "AC",
       command = lambda:allClear(),
       height=2, width=9).grid(row = 3 , column = 0 , sticky = E)


Button(gui,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "0",
       command = lambda:changeAns_val(0),
       height=2, width=21).grid(row = 7 , column = 0 ,
       columnspan=2 , sticky = E)

Button(gui,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "=",
       command = lambda:evaluateAnswer(),
       height=2, width=9).grid(row = 7 , column = 3, sticky = E)

       
gui.mainloop()