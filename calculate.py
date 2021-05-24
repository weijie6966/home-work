from tkinter import*
import tkinter
def miles_to_km():
    miles=float(input_v.get())
    km=miles*1.6
    lbl_km.config(text=f"{km}")
win=Tk()
win.minsize(width=500,height=380)
lbl_1=Label(text="enter value want to calculate")
lbl_1.pack()

input_v=Entry()
input_v.pack()

button=Button(text="calculate",command=miles_to_km)
button.pack()

lbl_km=Label(text="KM")
lbl_km.pack()

win.mainloop()