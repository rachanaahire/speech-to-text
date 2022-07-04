from tkinter import *
from tkinter import ttk
from mywindow import MyWindow

root = Tk()
style = ttk.Style(root)
style.theme_use('clam')
root.geometry("900x600")
MyWindow(root)

root.mainloop()
