from tkinter import *
from tkinter import ttk
from myentries import Entries
from mylabels import MyLabels
from viewentries import ViewEntries

class ScrollableFrame:
    def __init__(self, root, acc, opt):
        content = Frame(root, width=800, height=400)
        content.pack(fill=BOTH, expand=1)
        content.pack_propagate(0)
        content.place(relx=0.5, y=300, anchor=CENTER)
        
        # SCROLLBAR HORIZONTAL ad Vertical
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

        if opt == 'view':
            ViewEntries(root, acc, second_frame, 2) 
        if opt == 'insert':
            Entries(root, acc, second_frame, 2)
        if opt == 'update':
            print("uodateee")
        