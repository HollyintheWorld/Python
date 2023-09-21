from tkinter import * 

result=0

def change():
    global results
    input = int(E1.get())
    result = str(input*2.54)
    L4['text'] = str(result)


window = Tk()

L1 = Label(window, text="A program converts inch to cm")
L1.grid(row=0,column=0,columnspan=2)

L2 = Label(window, text="enter inch:")
L2.grid(row=1,column=0)

L3 = Label(window, text="cm")
L3.grid(row=2,column=0)

L4 = Label(window, text=result)
L4.grid(row=2,column=1)

E1= Entry(window)
E1.grid(row=1,column=1)

B1 = Button(window,text="convert!",command=change)
B1.grid(row=3,column=1)

window.mainloop()
