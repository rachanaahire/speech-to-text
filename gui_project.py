from tkinter import *
from tkinter import ttk
import time
import speech_recognition as sr
import sys

class Table:
    def __init__(self, bottom, rownum,cols):
        self.master = bottom
        self.cols = cols
        self.focusval = " "
        self.data = [[StringVar() for j in range (6)] for i in range(11)]
        for i in range(rownum, 10+rownum):
            for j in range(cols):
                self.cell = Entry(bottom, text=self.data[i-1][j], width=20)
                self.cell.grid(row=i,column=j)
        ttk.Button(root, text="RECORD", command=self.record, takefocus=0).place(x=100, y=450)
        ttk.Button(root, text="SAVE", command=self.getdata).place(x=200, y=450)

    def record(self):
        self.textdata = ""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening ...")
            audio = r.listen(source)
        try:
            print("You said: " + r.recognize_google(audio))
            self.textdata = r.recognize_google(audio)
            time.sleep(1)
        except sr.UnknownValueError:
            print("Google Speech Recognition couldn't understand")
            sys.exit()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        self.master.focus_get().insert(END, self.textdata)

    def getdata(self):
        final_data = [[self.data[i][j].get() for j in range (6)] for i in range(11)]
        print(final_data)

class MyWindow:
    def __init__(self):
        root.title("Text to Speech")
        self.accno = StringVar()

        ttk.Label(root, text="Account Number: ").place(x=50, y=50) #.grid(row=0, column=0,padx=10, pady=(20,0))
        ttk.Entry(root, textvariable=self.accno, width=30, font=('calibre', 10, 'normal')).place(x=170,y=50) #.grid(row=0,column=1,columnspan=2, pady=(20,0))
        ttk.Button(root, text="Left Page", command=self.showLeft).place(x=50,y=100)
        ttk.Button(root, text="Right Page").place(x=131,y=100)
    
    def showLeft(self):
        ttk.Label(root, text="\t     Left Page", width=30, relief='sunken', padding=(0,5,0,5)).place(relx=0.5, y=150, anchor=CENTER)
        bottom =Frame(root)
        bottom.place(relx=0.5,y=300, anchor=CENTER)

        #Table labels
        ttk.Label(bottom, text="       Time & Date", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=0)
        ttk.Label(bottom, text="       Airframe Hours", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=1)
        ttk.Label(bottom, text="       How found or\n       Aircrew Code", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=2)
        ttk.Label(bottom, text="    By Whom (Name)", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=3)
        ttk.Label(bottom, text="              SNOW", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=4)
        ttk.Label(bottom, text="    Reason for placing\n       unserviceable", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=5)

        Table(bottom, 1, 6)
  
    # def showRight(self):
    #     ttk.Label(root, text="\t     Right Page", width=30, relief='sunken', padding=(0,5,0,5)).place(relx=0.5, y=150, anchor=CENTER)
    #     bottom =Frame(root)
    #     bottom.place(relx=0.5,y=300, anchor=CENTER)

    #     #Table labels
    #     ttk.Label(bottom, text="       Time and Date\n       completed", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=0)
    #     ttk.Label(bottom, text="       Repair, storage\n       instructions,...", width=20, padding=(0,1,0,1), relief='solid').grid(row=0,column=1)
    #     ttk.Label(bottom, text="              Trade", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=2)
    #     ttk.Label(bottom, text="           Man hours", width=20, padding=(0,9,0,8.4), relief='solid').grid(row=0,column=3)

    #     Table(bottom, 1, 6)


root = Tk()
style = ttk.Style(root)
style.theme_use('clam')
root.geometry("900x600")
MyWindow()

root.mainloop()
