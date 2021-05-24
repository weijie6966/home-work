from tkinter import *
import math
# x=column
# y=row 
def clear():
    valueA.delete(0, 'end')
    valueB.delete(0, 'end')
    valueC.delete(0, 'end')

def calculate():
    a=int(valueA.get())
    b=int(valueB.get())
    c=int(valueC.get())
    #x1=((-(b))+ math.sqrt((math.pow(b,2) * (-4) * a * c))) /(2*a)
    #x2=((-(b))- math.sqrt((math.pow(b,2) * (-4) * a * c))) /(2*a)

    x1 = (-(b) + math.sqrt((b*b)-4*a*c))/(2*a)
    x2 = (-(b) - math.sqrt((b*b)-4*a*c))/(2*a)
    #x1=(-(b)+(math.sqrt((math.pow(b,2))*-4*a*c)))/2(a)
    
    #x2=(-(b)-(math.sqrt((math.pow(b,2))*-4*a*c)))/2(a)
    lblsolution.config(text=f"Solution: X={round(x1,3)} , X={round(x2,3)}")

win=Tk()
win.title("My first Python GUI ")
win.minsize(width=500,height=500)

lbltitel=Label(text="Quadratic Equation Solver")
lbltitel.place(x=170,y=0)

lblA=Label(text="A Value:")
lblA.place(x=30,y=30)

valueA=Entry()
valueA.place(x=90,y=30)

lblB=Label(text="B Value:")
lblB.place(x=30,y=60)

valueB=Entry()
valueB.place(x=90,y=60)

lblC=Label(text="C Value:")
lblC.place(x=30,y=90)

valueC=Entry()
valueC.place(x=90,y=90)

but_slove=Button(text="Slove",command=calculate)
but_slove.place(x=100,y=120)

but_clear=Button(text="Clear",command=clear)
but_clear.place(x=150,y=120)

lblsolution=Label(text="Solution:")
lblsolution.place(x=0,y=150)

win.mainloop()