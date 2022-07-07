from tkinter import *
from tkinter import ttk

class MyLabels:
    def __init__ (self, second_frame, j):
        if j:
                ttk.Label(second_frame, text="", width=15, padding=(0, 45, 0, 45), relief='solid').grid(row=0, column=0 , rowspan=2)

        ttk.Label(second_frame, text="\t\t\t\t\t\t\t\tAircraft Placed Unserviceable", width=144, padding=(
            0, 9, 0, 8.4), relief='solid').grid(row=0, column=j+0, columnspan=7)
        ttk.Label(second_frame, text="\t\t\t\tRecord of Work Carried Out, Replacements Etc",
                width=171, padding=(0, 9, 0, 8.4), relief='solid').grid(row=0, column=j+7, columnspan=6)
        ttk.Label(second_frame, text="Authorised signature \nCertified Defect Cleared \nor Transferred to \nMOD from 703/704",
                padding=(5, 23, 5, 23), relief='solid').grid(row=0, column=j+13, rowspan=2)

        # ROW2
        ttk.Label(second_frame, text="       Time & Date", width=20,
                padding=(0, 27, 0, 28), relief='solid').grid(row=1, column=j)
        ttk.Label(second_frame, text="       Airframe Hours", width=20,
                padding=(0, 27, 0, 28), relief='solid').grid(row=1, column=j+1)
        ttk.Label(second_frame, text="       How found or\n       Aircrew Code",
                width=20, padding=(0, 20, 0, 20), relief='solid').grid(row=1, column=j+2)
        ttk.Label(second_frame, text="    By Whom (Name)", width=20,
                padding=(0, 27, 0, 28), relief='solid').grid(row=1, column=j+3)
        ttk.Label(second_frame, text="              SNOW", width=20,
                padding=(0, 27, 0, 28), relief='solid').grid(row=1, column=j+4)
        ttk.Label(second_frame, text="    Reason for placing\n       unserviceable",
                width=20, padding=(0, 20, 0, 20), relief='solid').grid(row=1, column=j+5)
        ttk.Label(second_frame, text="       Job Number", width=20,
                padding=(0, 27, 0, 28), relief='solid').grid(row=1, column=j+6)
        ttk.Label(second_frame, text="Repairs, Storage instructions, Modifications, Special Technical Instructions \nServicing Instructions or other work including component Replacements.\nNote 1. State serial Numbers of Replacement items,  where applicable\n\t2. RN only. Quote Workshop Reference ORN.", padding=(6, 5, 6, 5), relief='solid').grid(row=1, column=j+7)
        ttk.Label(second_frame, text="       Signature of\n       Operative(s)",
                width=20, padding=(0, 20, 0, 20), relief='solid').grid(row=1, column=j+8)
        ttk.Label(second_frame, text="       Time and Date\n       Completed",
                width=20, padding=(0, 20, 0, 20), relief='solid').grid(row=1, column=j+9)
        ttk.Label(second_frame, text="              Trade", width=20, padding=(
            0, 27, 0, 28), relief='solid').grid(row=1, column=j+10)
        ttk.Label(second_frame, text="         Man Hours", width=20, padding=(
            0, 27, 0, 28), relief='solid').grid(row=1, column=j+11)
        ttk.Label(second_frame, text="       Signature of\n       Supervisor",
                width=20, padding=(0, 20, 0, 20), relief='solid').grid(row=1, column=j+12)
