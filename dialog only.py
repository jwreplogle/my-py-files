import tkinter as tk



def get_info():
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

    line1 = str(e1.get())
    line2 = str(e2.get())
    line3 = str(e3.get())
    line4 = str(e4.get())
  
    def clall():
        window.destroy()
        exit()

    def main():
        line1 = str(e1.get())
        line2 = str(e2.get())
        line3 = str(e3.get())
        line4 = str(e4.get())
        print ("Line 1 = ", line1)
        print ("Line 2 = ", line2)

    tk.Button(master, text='Quit', command=clall).grid(row=5, column=0, sticky=tk.W, pady=4)
    tk.Button(master, text='Show', command=main).grid(row=5, column=2, sticky=tk.W, pady=4)
  
    tk.mainloop()
    
def main():
    line1 = str(e1.get())
    line2 = str(e2.get())
    line3 = str(e3.get())
    line4 = str(e4.get())
    print ("Line 1 = ", line1)
    print ("Line 2 = ", line2)
    
    
get_info()    
