 #import
from tkinter import *
import tkinter as tk
from tkinter import ttk

# tkinter entry
master = tk.Tk()

master.title("Text for 4 x 20")
tk.Label(master, text="Enter Text To Display on LED; 1-Left 2-Center 3-Right", fg='red',font=("Helvetica", 14)).grid(row=0)
master.geometry('800x400')
c1=StringVar()
c2=StringVar()
c3=StringVar()
c4=StringVar()
c1.set(1)
c2.set(1)
c3.set(1)
c4.set(1)
cdata=("1", "2", "3")

cb1=ttk.Combobox(master, textvariable=c1, values=cdata, width=3).place(x=1, y=50)
cb2=ttk.Combobox(master, textvariable=c2, values=cdata, width=3).place(x=1, y=90)
cb3=ttk.Combobox(master, textvariable=c3, values=cdata, width=3).place(x=1, y=130)
cb4=ttk.Combobox(master, textvariable=c4, values=cdata, width=3).place(x=1, y=170)

tk.Label(master, text="Display Line 1:", width=20,font=("Helvetica", 14)).place(x=80, y=45)
tk.Label(master, text="Display Line 2:", width=20,font=("Helvetica", 14)).place(x=80, y=85)
tk.Label(master, text="Display Line 3:", width=20,font=("Helvetica", 14)).place(x=80, y=125)
tk.Label(master, text="Display Line 4:", width=20,font=("Helvetica", 14)).place(x=80, y=165)

e1 = tk.Entry(master).place(x=400, y=50)
e2 = tk.Entry(master).place(x=400, y=90)
e3 = tk.Entry(master).place(x=400, y=130)
e4 = tk.Entry(master).place(x=400, y=170)

def clall():
    master.destroy()

def stext():
    line1 = str(e1.get())
    line2 = str(e2.get())
    line3 = str(e3.get())
    line4 = str(e4.get())
    cc1 = int(c1.get())
    cc2 = int(c2.get())
    cc3 = int(c3.get())
    cc4 = int(c4.get())
    print("cb1= ", cc1)
    print("cb2= ", cc2)
    print("cb3= ", cc3)
    print("cb4= ", cc4)
    print ("Line 1 = ", line1)
    print ("Line 2 = ", line2)
    print ("Line 3 = ", line3)
    print ("Line 4 = ", line4)


tk.Button(master, text='Quit', command=clall).place(x=1, y=250)
tk.Button(master, text='Show', command=stext).place(x=450, y=250)



tk.mainloop()

