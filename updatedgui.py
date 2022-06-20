from tkinter import *
from tkinter import ttk
from vosk import Model, KaldiRecognizer
import pyaudio

class Entries:
    def __init__(self, second_frame, i):
        self.row_num = i
        self.second_frame = second_frame
        self.create_row(0, 7, 15)
        self.create_row(7, 8, 50)
        self.create_row(8, 12, 15)
        self.create_row(12, 13, 17)

        ttk.Button(root, text="RECORD", command=self.record, takefocus=0).place(x=100, y=550)
        ttk.Button(root, text = "SAVE", command=lambda w=second_frame: self.get_all_entry_widgets_text_content(w)).place(x=200, y=550)
        ttk.Button(root, text="ADD ROW", command=self.add_row).place(x=300, y=550)
    
    def create_row(self, scol, ecol, wid):
            for j in range(scol, ecol):
                self.cell = Text(self.second_frame, height=3, width=wid)
                self.cell.grid(row=self.row_num,column=j)

    def get_all_entry_widgets_text_content(self, parent_widget):
        children_widgets = parent_widget.winfo_children()
        mydata = [child_widget.get(1.0, 'end')[:-1] for child_widget in children_widgets if child_widget.winfo_class() == 'Text']
        mdata = [mydata[i:i+13] for i in range(0, len(mydata), 13)]
        print("Account number: ", self.acc)
        print("Data: ",mdata)

    def record(self):
        self.textdata = ""
        model = Model(r"D:\study\python\text to speech project\TTS project\vosk-model-small-en-us-0.15")
        recognizer = KaldiRecognizer(model, 16000)

        mic = pyaudio.PyAudio()
        stream =  mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        bol = True

        while bol:
            data= stream.read(4096)
            if recognizer.AcceptWaveform(data):
                self.textdata = recognizer.Result()
                print(self.textdata)
                self.second_frame.focus_get().insert(END, self.textdata[14:-3])
                bol= False
        
    
    def add_row(self):
        self.row_num = self.row_num + 1
        Entries(self.second_frame, self.row_num)

class MyWindow:
    def __init__(self):
        root.title("Text to Speech")
        self.accno = StringVar()
        self.bottom = None

        ttk.Label(root, text="Account Number: ").place(x=50, y=50)
        ttk.Entry(root, textvariable=self.accno, width=30, font=('calibre', 10, 'normal')).place(x=170,y=50)

        #Updates
        content = Frame(root, width=800, height=400)
        content.pack(fill=BOTH, expand=1)
        content.pack_propagate(0)
        content.place(relx=0.5,y=300, anchor=CENTER)

        #Create main frame
        main_frame = Frame(content)
        main_frame.pack(fill=BOTH, expand=1)

        #Create canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=TOP,fill=BOTH, expand= 1)

        # create scrollbar to thhe canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
        my_scrollbar.pack(side=BOTTOM, fill=X)

        #configure canvas
        my_canvas.configure(xscrollcommand =my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        #create another frame inside the canvas
        second_frame = Frame(my_canvas)

        #add that new frame to a window in canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")

        #TABLE 

        #ROW1
        ttk.Label(second_frame, text="\t\t\t\t\t\t\t\tAircraft Placed Unserviceable", width=144, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=0, columnspan=7)
        ttk.Label(second_frame, text="\t\t\t\tRecord of Work Carried Out, Replacements Etc", width=150, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=7, columnspan=5)
        ttk.Label(second_frame, text="Authorised signature \nCertified Defect Cleared \nor Transferred to \nMOD from 703/704", padding=(5,23,5,23), relief='solid').grid(row=0,column=12, rowspan=2)

        #ROW2
        ttk.Label(second_frame, text="       Time & Date", width=20, padding=(0,27,0,28), relief='solid').grid(row=1,column=0)
        ttk.Label(second_frame, text="       Airframe Hours", width=20, padding=(0,27,0,28), relief='solid').grid(row=1,column=1)
        ttk.Label(second_frame, text="       How found or\n       Aircrew Code", width=20, padding=(0,20,0,20), relief='solid').grid(row=1,column=2)
        ttk.Label(second_frame, text="    By Whom (Name)", width=20, padding=(0,27,0,28), relief='solid').grid(row=1,column=3)
        ttk.Label(second_frame, text="              SNOW", width=20, padding=(0,27,0,28), relief='solid').grid(row=1,column=4)
        ttk.Label(second_frame, text="    Reason for placing\n       unserviceable", width=20, padding=(0,20,0,20), relief='solid').grid(row=1,column=5)
        ttk.Label(second_frame, text="       Job Number", width=20, padding=(0,27,0,28), relief='solid').grid(row=1,column=6)
        ttk.Label(second_frame, text="Repairs, Storage instructions, Modifications, Special Technical Instructions \nServicing Instructions or other work including component Replacements.\nNote 1. State serial Numbers of Replacement items,  where applicable\n\t2. RN only. Quote Workshop Reference ORN.", padding=(6,5,6,5), relief='solid').grid(row=1,column=7)
        ttk.Label(second_frame, text="       Signature of\n       Operative(s)", width=20, padding=(0,20,0,20), relief='solid').grid(row=1,column=8)
        ttk.Label(second_frame, text="       Time and Date\n       Completed", width=20, padding=(0,20,0,20), relief='solid').grid(row=1,column=10)
        ttk.Label(second_frame, text="              Trade", width=20, padding=(0,27,0,28), relief='solid').grid(row=1,column=9)
        ttk.Label(second_frame, text="         Man Hours", width=20, padding=(0,27,0,28), relief='solid').grid(row=1,column=10)
        ttk.Label(second_frame, text="       Signature of\n       Supervisor", width=20, padding=(0,20,0,20), relief='solid').grid(row=1,column=11)
        
        Entries(second_frame,2)


root = Tk()
style = ttk.Style(root)
style.theme_use('clam')
root.geometry("900x600")
MyWindow()

root.mainloop()
