import tkinter as tk

def show_entry_fields():
    print("Line 1: %s\nLine 2: %s\nLine 3: %s\nLine 4: %s" % (e1.get(), e2.get(), e3.get(), e4.get()))

master = tk.Tk()
tk.Label(master, text="Line 1").grid(row=0)
tk.Label(master, text="Line 2").grid(row=1)
tk.Label(master, text="Line 3").grid(row=2)
tk.Label(master, text="Line 4").grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


tk.Button(master, text='Quit', command=master.quit).grid(row=5, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=5, column=2, sticky=tk.W, pady=4)

tk.mainloop()