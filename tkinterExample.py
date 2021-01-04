import tkinter
from tkinter import *
import tkinter.messagebox
top = Tk()
L1 = Label(top, text="Hi")
L1.pack(side = LEFT)
E1 = Entry(top, bd=5)
E1.pack(side = RIGHT)
B=Button(top, text ="Hello")
B.pack()

top.mainloop()
