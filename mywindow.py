from tkinter import *
from tkinter import ttk
from myentries import Entries
from mylabels import MyLabels
from scrollableframe import ScrollableFrame

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
            self.clear_frame(self.main_frame)

        # ScrollableFrame(self.root, self.accno.get(), 'view')
        
        # SCROLLBAR HORIZONTAL ad Vertical
        # content = Frame(self.root, width=800, height=400)
        # content.pack(fill=BOTH, expand=1)
        # content.pack_propagate(0)
        # content.place(relx=0.5, y=300, anchor=CENTER)

        # # Create main frame
        # self.main_frame = Frame(content)
        # self.main_frame.pack(fill=BOTH, expand=1)

        # # Create canvas
        # my_canvas = Canvas(self.main_frame)
        # my_canvas.pack(side=TOP, fill=BOTH, expand=1)

        # # create scrollbar to thhe canvas
        # my_scrollbar = ttk.Scrollbar(
        #     self.main_frame, orient=HORIZONTAL, command=my_canvas.xview)
        # my_scrollbar.pack(side=BOTTOM, fill=X)

        # # configure canvas
        # my_canvas.configure(xscrollcommand=my_scrollbar.set)
        # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        #     scrollregion=my_canvas.bbox("all")))

        # # create another frame inside the canvas
        # second_frame = Frame(my_canvas)

        # # add that new frame to a window in canvas
        # my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # # TABLE
        # MyLabels(second_frame)
        # Entries(self.root, self.accno.get(), second_frame, 2)
        

    def child_insert_window(self):
        if self.main_frame != None:
            self.clear_frame(self.main_frame)
        
        # ScrollableFrame(self.root, self.accno.get(), 'insert')
        # SCROLLBAR HORIZONTAL
        content = Frame(self.root, width=800, height=400)
        content.pack(fill=BOTH, expand=1)
        content.pack_propagate(0)
        content.place(relx=0.5, y=300, anchor=CENTER)

        # Create main frame
        self.main_frame = Frame(content)
        self.main_frame.pack(fill=BOTH, expand=1)

        # Create canvas
        my_canvas = Canvas(self.main_frame)
        my_canvas.pack(side=TOP, fill=BOTH, expand=1)

        # create scrollbar to thhe canvas
        my_scrollbar = ttk.Scrollbar(
            self.main_frame, orient=HORIZONTAL, command=my_canvas.xview)
        my_scrollbar.pack(side=BOTTOM, fill=X)

        # configure canvas
        my_canvas.configure(xscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
            scrollregion=my_canvas.bbox("all")))

        # create another frame inside the canvas
        second_frame = Frame(my_canvas)

        # add that new frame to a window in canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # TABLE
        MyLabels(second_frame)
        Entries(self.root, self.accno.get(), second_frame, 2)

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

        