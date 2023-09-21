from tkinter import *

sum=0

def plus():
    global sum
    input=int(e1.get())
    sum += input
    l2['text'] = str(sum)

def minus():
    global sum
    input = int(e1.get())
    sum +=input
    l2['text'] = str(sum)

def reset():
    l2['text']= 0

window = Tk() 

l1 = Label(window, text="current sum")
l1.grid(row=0, column=0)

l2 = Label(window, text=sum)
l2.grid(row=0, column=1)

e1 = Entry(window)
e1.grid(row=1, column=0, columnspan=3)

b1 = Button(window,text="Plus (+)", command=plus)
b1.grid(row=2,column=0)

b2 = Button(window,text="Minus (-)", command=minus)
b2.grid(row=2,column=1)

b3 = Button(window,text="Initialize the sum",command=reset)
b3.grid(row=2,column=2)

window.mainloop()
