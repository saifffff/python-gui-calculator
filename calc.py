from tkinter import *
import math


ansValGlobal = ""
ansLabelGlobal = ""

root = Tk()

root.title('Calculator by Saif Khan')

p1 = PhotoImage(file='shiats.png')
root.iconphoto(False,p1)

Ans_val = StringVar()

Entry(root, font=('futura', 25, 'bold'),
textvariable = Ans_val,
justify = LEFT).grid(columnspan=4, ipadx=120)

answerFinalLabel = StringVar()

Entry(root, font=('futura', 25, 'bold'),
textvariable = answerFinalLabel,
justify = LEFT).grid(columnspan = 4 , ipadx=120)


def changeAns_val(entry):
    global ansValGlobal
    global ansLabelGlobal 
    ansValGlobal = ansValGlobal + str(entry)
    ansLabelGlobal = ansValGlobal
    Ans_val.set(ansValGlobal)


def clearAns_val():
    global ansValGlobal
    global ansLabelGlobal
    ansLabelGlobal = ansValGlobal
    ansValGlobal = ""
    Ans_val.set(ansValGlobal)



def evaluateSquareRoot():
    global ansValGlobal
    global ansLabelGlobal
    try:
        sqrtAnswer = math.sqrt(eval(str(ansLabelGlobal)))
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
    global ansLabelGlobal
    ansValGlobal = ""
    ansLabelGlobal = ""
    Ans_val.set("")
    answerFinalLabel.set("")



def createButton(txt,x,y):
    Button(root, font=('futura', 15, 'bold'),
           padx=16,pady=16,text = str(txt),
           command = lambda:changeAns_val(txt),
           height = 2, width=9).grid(row = x , column = y, sticky=E)


buttons = ['AC','√','%','/','7','8','9','*','4','5','6','-','1','2','3','+','','','.','']
buttonsListTraversalCounter = 0

for i in range(3,8):
    for j in range(0,4):
        createButton(buttons[buttonsListTraversalCounter],i,j)
        buttonsListTraversalCounter =buttonsListTraversalCounter + 1

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "√",
       command = lambda:evaluateSquareRoot(),
       height=2, width=9).grid(row = 3 , column = 1, sticky = E)



Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "AC",
       command = lambda:allClear(),
       height=2, width=9).grid(row = 3 , column = 0 , sticky = E)
       

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "0",
       command = lambda:changeAns_val(0),
       height=2, width=21).grid(row = 7 , column = 0 ,
       columnspan=2 , sticky = E)

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "=",
       command = lambda:evaluateAnswer(),
       height=2, width=9).grid(row = 7 , column = 3, sticky = E)

       
root.mainloop()