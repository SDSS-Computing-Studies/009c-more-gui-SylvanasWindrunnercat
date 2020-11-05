#! python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk
import math

window = tk.Tk()
window.title("Triangle Calculater")
window.geometry("450x150")

def Triangle():
    a = e1.get()
    a = float(a)
    b = e1.get()
    b = float(b)
    c = e3.get()
    c = float(c)
    h = e4.get()
    h = float(h)
    
    if h == 0:
        a = int(a)
        b = int(b)
        c = int(c)
        s = (a + b + c) / 2
        d = math.sqrt(s (s - a) * (s - b) * (s - c))
    elif a == 0 or b == 0 or c == 0:
        answer = "Erorr,lack information"
    else:
        b = int(b)
        h = int(h)
        d = b * h / 2
    a_entry.delete(0,END)
    a_entry.insert(0,answer)

l0 = tk.Label(window,text= "If you don't know the length,please enter 0 to instead")
l1 = tk.Label(window,text = "length of side1")
e1 = tk.Entry(window,width = 10)
l2 = tk.Label(window,text = "length of side2")
e2 = tk.Entry(window,width = 10)
l3 = tk.Label(window,text = "length of side3")
e3 = tk.Entry(window,width = 10)
l4 = tk.Label(window,text = "length of high")
e4 = tk.Entry(window,width = 10)
b1 = tk.Button(window,text = "Calculate",command = Triangle)

l0.grid(row = 1,column = 1)
l1.grid(row = 2,column = 1)
e1.grid(row = 2,column = 2)
l2.grid(row = 3,column = 1)
e2.grid(row = 3,column = 2)
l3.grid(row = 4,column = 1)
e3.grid(row = 4,column = 2)
l4.grid(row = 5,column = 1)
e4.grid(row = 5,column = 2)
b1.grid(row = 1,column = 3)

window.mainloop()
