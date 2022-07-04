from tkinter import *
from tkinter import ttk
from scrollableframe import ScrollableFrame
from common_functions import clear_frame

class MyWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Change of Serviceability Log")
        self.accno = StringVar()
        self.bottom = None

        ttk.Label(self.root, text="Account Number: ").place(x=50, y=50)
        ttk.Entry(self.root, textvariable=self.accno, width=30, font=('calibre', 10, 'normal')).place(x=170, y=50)
        ttk.Button(self.root, text="SUBMIT",command=self.mymenu).place(x=400, y=50)
        
    
    def mymenu(self):
        self.main_frame = None
        ttk.Button(self.root, text="INSERT", command=self.child_insert_window).place(x=518, y=50)
        ttk.Button(self.root, text="VIEW", command= self.child_view_window).place(x=600, y=50)

    def child_view_window(self):
        if self.main_frame != None:
            clear_frame(self.main_frame)
        ScrollableFrame(self.root, self.accno.get(), 'view')

    def child_insert_window(self):
        if self.main_frame != None:
            clear_frame(self.main_frame)
        ScrollableFrame(self.root, self.accno.get(), 'insert')


        