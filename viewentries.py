from tkinter import *
from tkinter import ttk
from myentries import Entries
from mylabels import MyLabels
import pandas as pd
import openpyxl

class ViewEntries:
    def __init__(self, root, acc, second_frame, row_no):
        self.row_no = row_no
        self.second_frame = second_frame
        self.root = root
        self.row_range = 0
        self.acc = acc
        self.wid = {7: 50, 13: 17}
        book = openpyxl.load_workbook('Report.xlsx')
        self.sheets = {ws.title: ws for ws in book.worksheets}
        if self.acc in self.sheets:
            self.mrows = self.sheets[self.acc].max_row - 1
            self.mcols = self.sheets[self.acc].max_column
            self.my_display(0)
        else:
            print("hhhh")
            ttk.Label(self.second_frame, text="No records found").grid(row=self.row_no, column=0)

        print(self.row_range)

    def my_display(self, offset):
        print("pooo",offset)
        limit = 3
        df_acc = pd.read_excel('Report.xlsx', sheet_name=self.acc)
        for i in range(self.row_no, limit+self.row_no):
            for j in range(1, self.mcols):
                mywid = 15 if (j-1 not in self.wid) else self.wid[j-1]
                cell = Text(self.second_frame, height=3, width=mywid)
                cell.grid(row=i, column=j-1)
                sen = ""
                if (i-self.row_no+offset>=self.mrows):
                    cell.insert(END, "")
                else:
                    sen = "" if pd.isna(df_acc.iloc[i-self.row_no+offset][j]) else df_acc.iloc[i-self.row_no+offset][j]
                    cell.insert(END, sen)

        back = offset - limit # This value is used by Previous button
        next = offset + limit  # This value is used by Next button       
        b1 = ttk.Button(self.root, text='Next >', command=lambda: self.my_display(next))
        b1.place(x=40,y=550)
        b2 = ttk.Button(self.root, text='< Prev', command=lambda: self.my_display(back))
        b2.place(x=150,y=550)
        if(self.mrows+1 <= next): 
            b1["state"]="disabled" # disable next button
        else:
            b1["state"]="active"  # enable next button
            
        if(back >= 0):
            b2["state"]="active"  # enable Prev button
        else:
            b2["state"]="disabled"# disable Prev button

# root = Tk()
# style = ttk.Style(root)
# style.theme_use('clam')
# root.geometry("900x600")

# # 3

# # for x in range(self.mrows-1):
# #     print(df_acc.iloc[x][0])

# content = Frame(root, width=800, height=400)
# content.pack(fill=BOTH, expand=1)
# content.pack_propagate(0)
# content.place(relx=0.5, y=300, anchor=CENTER)

# # Create main frame
# main_frame = Frame(content)
# main_frame.pack(fill=BOTH, expand=1)

# # Create canvas
# my_canvas = Canvas(main_frame)

# # create scrollbar to thhe canvas
# my_scrollbar_v = ttk.Scrollbar(
#     main_frame, orient=VERTICAL, command=my_canvas.yview)
# my_scrollbar_v.pack(side=RIGHT, fill=Y)

# my_scrollbar_h = ttk.Scrollbar(
#     main_frame, orient=HORIZONTAL, command=my_canvas.xview)
# my_scrollbar_h.pack(side=BOTTOM, fill=X)

# # configure canvas
# my_canvas.configure(yscrollcommand=my_scrollbar_v.set)
# my_canvas.configure(xscrollcommand=my_scrollbar_h.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
#     scrollregion=my_canvas.bbox("all")))


# my_canvas.pack(side=TOP, fill=BOTH, expand=1)

# # create another frame inside the canvas
# second_frame = Frame(my_canvas)

# # add that new frame to a window in canvas
# my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# MyLabels(second_frame)
# ViewEntries(root, second_frame)

# root.mainloop()
