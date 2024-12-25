#ex:creating a basic GUI application
#Import module
from tkinter import *
# create root window
root = Tk()
#root window tittle and dimension
root.title("My First Tkinter App")
#set geometry(widthxheight)
root.geometry('350x200')
root.mainloop()




import tkinter as tk
window=tk.Tk()
lbl1=tk.Label(master=window,text="HELLO WORLD")
lbl1.pack()
window.mainloop()
