from tkinter import*
import tkinter
from tkinter import messagebox

window= Tk()
window.title("My first Python GUI ")
window.minsize(width=500,height=500)

#1 button
#2 label
#3 entry

def helloCallBack():
    print("Hello World")
    messagebox.showinfo("MY world","say hello")

button=Button(text="Click Me!",command=helloCallBack)
button.pack()

my_label=Label(text="I am the label",font=("Arial",36,"bold"))
my_label.pack()

input=Entry()
input.pack()

second_lbl=Label(text="~second label~")
second_lbl.pack()

window.mainloop()