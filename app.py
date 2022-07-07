from tkinter import *
from tkinter import ttk
from mywindow import MyWindow

root = Tk()
style = ttk.Style(root)
style.theme_use('clam')
root.state('zoomed')
MyWindow(root)

root.mainloop()
