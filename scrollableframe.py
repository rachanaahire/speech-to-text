from tkinter import *
from tkinter import ttk
from myentries import Entries
from mylabels import MyLabels
from viewentries import ViewEntries

class ScrollableFrame:
    def __init__(self, root, opt, acc, index=None):
        content = Frame(root, width=1000, height=400)
        content.pack(fill=BOTH, expand=1)
        content.pack_propagate(0)
        content.place(relx=0.5, y=375, anchor=CENTER)

        # Create main frame
        main_frame = Frame(content)
        main_frame.pack(fill=BOTH, expand=1)

        # Create canvas
        my_canvas = Canvas(main_frame)

        # create scrollbar to thhe canvas
        my_scrollbar_v = ttk.Scrollbar(
            main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar_v.pack(side=RIGHT, fill=Y)

        my_scrollbar_h = ttk.Scrollbar(
            main_frame, orient=HORIZONTAL, command=my_canvas.xview)
        my_scrollbar_h.pack(side=BOTTOM, fill=X)

        # configure canvas
        my_canvas.configure(yscrollcommand=my_scrollbar_v.set)
        my_canvas.configure(xscrollcommand=my_scrollbar_h.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
            scrollregion=my_canvas.bbox("all")))


        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # create another frame inside the canvas
        second_frame = Frame(my_canvas)

        # add that new frame to a window in canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # TABLE

        if opt == 'view':
            MyLabels(second_frame,1)
            ViewEntries(root, acc, second_frame, 2) 

        if opt == 'insert':
            MyLabels(second_frame,0)
            Entries(root, acc, second_frame, 2, 'insert', None)

        if opt == 'update':
            MyLabels(second_frame,0)
            Entries(root, acc, second_frame, 2, 'update', index)


        