from tkinter import *
exp=""
def show(num):
    global exp
    exp=exp+str(num)
    equ.set(exp)
def equal():
    try:
        global exp
        total=str(eval(exp))
        equ.set(total)
        exp=""
    except:
        equ.set("error")
        exp=""
def clear():
    global exp
    exp=""
    equ.set("")
root=Tk();
root.title("Calculator")
root.geometry("365x165")
root.configure(background="light blue")
equ=StringVar()
enterequ=Entry(root,textvariable=equ)
exp=exp+str(equ)
enterequ.grid(columnspan=4,ipadx=75) #columnspan to represent the number of columns in a root box
equ.set("Enter the exp")
b1=Button(root,text="1",fg="black",bg="light green",command=lambda: show(1),height=2,width=9)
b1.grid(row=2, column=0)
b2=Button(root,text="2",fg="black",bg="light green",command=lambda: show(2),height=2,width=9)
b2.grid(row=2, column=1)
b3=Button(root,text="3",fg="black",bg="light green",command=lambda: show(3),height=2,width=9)
b3.grid(row=2, column=2)
b4=Button(root,text="4",fg="black",bg="light green",command=lambda: show(4),height=2,width=9)
b4.grid(row=3, column=0)
b5=Button(root,text="5",fg="black",bg="light green",command=lambda: show(5),height=2,width=9)
b5.grid(row=3, column=1)
b6=Button(root,text="6",fg="black",bg="light green",command=lambda: show(6),height=2,width=9)
b6.grid(row=3, column=2)
b7=Button(root,text="7",fg="black",bg="light green",command=lambda: show(7),height=2,width=9)
b7.grid(row=4, column=0)
b8=Button(root,text="8",fg="black",bg="light green",command=lambda: show(8),height=2,width=9)
b8.grid(row=4, column=1)
b9=Button(root,text="9",fg="black",bg="light green",command=lambda: show(9),height=2,width=9)
b9.grid(row=4, column=2)
b0=Button(root,text="0",fg="black",bg="light green",command=lambda: show(0),height=2,width=9)
b0.grid(row=5, column=1)
bc=Button(root,text="=",fg="black",bg="light green",command=equal,height=2,width=9)
bc.grid(row=5, column=2)
bp=Button(root,text="+",fg="black",bg="light green",command=lambda: show("+"),height=2,width=9)
bp.grid(row=2, column=3)
bm=Button(root,text="-",fg="black",bg="light green",command=lambda: show("-"),height=2,width=9)
bm.grid(row=3, column=3)
bmul=Button(root,text="*",fg="black",bg="light green",command=lambda: show("*"),height=2,width=9)
bmul.grid(row=4, column=3)
bd=Button(root,text="/",fg="black",bg="light green",command=lambda: show("/"),height=2,width=9)
bd.grid(row=5, column=3)
root.mainloop()