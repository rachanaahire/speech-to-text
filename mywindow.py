from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from scrollableframe import ScrollableFrame
from common_functions import clear_frame

class MyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Change of Serviceability Log")
        self.accno = StringVar()
        self.bottom = None

        ttk.Label(self.root, text="Change of Serviceability Log", font=('calibre', 20)).place(x=500, y=30)
        ttk.Label(self.root, text="Account Number: ").place(x=200, y=110)
        ttk.Entry(self.root, textvariable=self.accno, width=30, font=('calibre', 10, 'normal')).place(x=320, y=110)
        self.main_frame = None
        ttk.Button(self.root, text="INSERT", command=self.child_insert_window).place(x=700, y=110)
        ttk.Button(self.root, text="VIEW", command= self.child_view_window).place(x=778, y=110)

    def child_view_window(self):
        if self.main_frame != None:
            clear_frame(self.main_frame)
        if (self.accno.get()):
            ScrollableFrame(self.root, 'view', self.accno.get())
        else:
            messagebox.showerror('Input Error', 'Please Enter Account Number!')

    def child_insert_window(self):
        if self.main_frame != None:
            clear_frame(self.main_frame)
        if (self.accno.get()):
            ScrollableFrame(self.root, 'insert', self.accno.get())
        else:
            messagebox.showerror('Input Error', 'Please Enter Account Number!')


        