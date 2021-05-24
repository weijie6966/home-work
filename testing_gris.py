from tkinter import *

def calulate():
    base=float(enterb.get())
    height=float(enterh.get())
    ans=(base*height)/2
    lblresult.config(text=f"Area of Triangle={ans}")

win=Tk()
win.title("My first Python GUI ")
win.minsize(width=500,height=500)

my_label=Label()
my_label.config(text="Enter base:")
my_label.grid(column=0,row=0)

my_label_2=Label()
my_label_2.config(text="Enter height:")
my_label_2.grid(column=0,row=1)

enterb=Entry()
enterb.grid(column=1,row=0)

enterh=Entry()
enterh.grid(column=1,row=1)

newbutton=Button(text="new button",command=calulate)
newbutton.grid(rowspan=2,column=3,row=0)

lblresult=Label(text="Area of Triangle=")
lblresult.grid(columnspan=3,column=0,row=2)


win.mainloop()