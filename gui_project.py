from tkinter import *
from tkinter import ttk
import time
from numpy import histogram_bin_edges
import speech_recognition as sr
import sys
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
        
        # self.text1 = Text(second_frame, height=3, width=15)
        # self.text1.grid(row=i, column=0)
        # self.text2 = Text(second_frame, height=3, width=15)
        # self.text2.grid(row=i, column=1)
        # self.text3 = Text(second_frame, height=3, width=15)
        # self.text3.grid(row=i, column=2)
        # self.text4 = Text(second_frame, height=3, width=15)
        # self.text4.grid(row=i, column=3)
        # self.text5 = Text(second_frame, height=3, width=15)
        # self.text5.grid(row=i, column=4)
        # self.text6 = Text(second_frame, height=3, width=15)
        # self.text6.grid(row=i, column=5)
        # self.text7 = Text(second_frame, height=3, width=15)
        # self.text7.grid(row=i, column=6)
        # self.text8 = Text(second_frame, height=3, width=50)
        # self.text8.grid(row=i, column=7)
        # self.text9 = Text(second_frame, height=3, width=15)
        # self.text9.grid(row=i, column=8)
        # self.text10 = Text(second_frame, height=3, width=15)
        # self.text10.grid(row=i, column=9)
        # self.text11 = Text(second_frame, height=3, width=15)
        # self.text11.grid(row=i, column=10)
        # self.text12 = Text(second_frame, height=3, width=15)
        # self.text12.grid(row=i, column=11)
        # self.text13 = Text(second_frame, height=3, width=17)
        # self.text13.grid(row=i, column=12)

        ttk.Button(root, text="RECORD", command=self.record, takefocus=0).place(x=100, y=550)
        ttk.Button(root, text = "SAVE", command=lambda w=second_frame: self.get_all_entry_widgets_text_content(w)).place(x=200, y=550)
        ttk.Button(root, text="ADD ROW", command=self.add_row).place(x=300, y=550)

    def create_row(self, scol, ecol, wid):
            for j in range(scol, ecol):
                self.cell = Text(self.second_frame, height=3, width=wid)
                self.cell.grid(row=self.row_num,column=j)

    def get_all_entry_widgets_text_content(self, parent_widget):
        # mydata = []
        children_widgets = parent_widget.winfo_children()
        mydata = [child_widget.get(1.0, 'end')[:-1] for child_widget in children_widgets if child_widget.winfo_class() == 'Text']
        print(mydata)
        # for child_widget in children_widgets:
        #     if child_widget.winfo_class() == 'Text':
                # print(child_widget.get(1.0, 'end'))


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
                bol= False
        self.second_frame.focus_get().insert(END, self.textdata[14:-3])
    
    def add_row(self):
        self.row_num = self.row_num + 1
        Entries(self.second_frame, self.row_num)

class Table:
    def __init__(self, second_frame, acc_no, rownum, cols):
        # self.bottom = data[0]
        self.bottom = second_frame
        self.accno = acc_no
        # self.option = data[2]
        self.cols = cols
        self.focusval = " "
        self.data = [[StringVar() for j in range (cols)] for i in range(11)]
        for i in range(rownum, 10+rownum):
            for j in range(cols):
                # self.cell = Text(self.bottom, text=self.data[i-1][j], width=20)
                # self.cell.grid(row=i,column=j)
                self.cell = Entry(self.bottom, text=self.data[i-1][j], width=20)
                self.cell.grid(row=i,column=j)
        ttk.Button(root, text="RECORD", command=self.record, takefocus=0).place(x=100, y=550)
        ttk.Button(root, text="SAVE", command=self.getdata).place(x=200, y=550)

    def record(self):
        self.textdata = ""
        # r = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("listening ...")
        #     audio = r.listen(source)
        # try:
        #     print("You said: " + r.recognize_google(audio))
        #     self.textdata = r.recognize_google(audio)
        #     time.sleep(1)
        # except sr.UnknownValueError:
        #     print("Google Speech Recognition couldn't understand")
        #     sys.exit()
        # except sr.RequestError as e:
        #     print("Could not request results from Google Speech Recognition service; {0}".format(e))
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
                bol= False
        self.bottom.focus_get().insert(END, self.textdata[14:-3])

    def getdata(self):
        final_data = [[self.data[i][j].get() for j in range (self.cols)] for i in range(11)]
        print("Account number is ", self.accno.get())
        # print(self.option.title() + " Page Data: ")
        print(final_data)

class MyWindow:
    def __init__(self):
        root.title("Text to Speech")
        self.accno = StringVar()
        self.bottom = None

        ttk.Label(root, text="Account Number: ").place(x=50, y=50) #.grid(row=0, column=0,padx=10, pady=(20,0))
        ttk.Entry(root, textvariable=self.accno, width=30, font=('calibre', 10, 'normal')).place(x=170,y=50) #.grid(row=0,column=1,columnspan=2, pady=(20,0))
        # ttk.Button(root, text="Left Page", command=self.showLeft).place(x=50,y=100)
        # ttk.Button(root, text="Right Page", command=self.showRight).place(x=131,y=100)

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
        # Table(second_frame, self.accno, 2, 13)
        Entries(second_frame,2)


    def showLeft(self):
        ttk.Label(root, text="\t     Left Page", width=30, relief='sunken', padding=(0,5,0,5)).place(relx=0.5, y=150, anchor=CENTER)
        bottom =Frame(root)
        self.bottom = bottom
        bottom.place(relx=0.5,y=300, anchor=CENTER)

        #Table labels
        ttk.Label(bottom, text="       Time & Date", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=0)
        ttk.Label(bottom, text="       Airframe Hours", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=1)
        ttk.Label(bottom, text="       How found or\n       Aircrew Code", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=2)
        ttk.Label(bottom, text="    By Whom (Name)", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=3)
        ttk.Label(bottom, text="              SNOW", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=4)
        ttk.Label(bottom, text="    Reason for placing\n       unserviceable", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=5)

        data = [bottom, self.accno, 'left']
        Table(data, 1, 6)
  
    def showRight(self):
        if self.bottom != None:
            self.clear_frame(self.bottom)
        ttk.Label(root, text="\t     Right Page", width=30, relief='sunken', padding=(0,5,0,5)).place(relx=0.5, y=150, anchor=CENTER)
        bottom =Frame(root)
        bottom.place(relx=0.5,y=300, anchor=CENTER)

        #Table labels
        ttk.Label(bottom, text="       Time and Date\n       completed", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=0)
        ttk.Label(bottom, text="       Repair, storage\n       instructions,...", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=1)
        ttk.Label(bottom, text="              Trade", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=2)
        ttk.Label(bottom, text="           Man hours", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=3)

        data = [bottom, self.accno, 'right']
        Table(data, 1, 4)
    
    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()


root = Tk()
style = ttk.Style(root)
style.theme_use('clam')
root.geometry("900x600")
MyWindow()

root.mainloop()
