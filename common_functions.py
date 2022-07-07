
def getnum(mystr):
    # print("=>",mystr)
    num = ""
    for c in mystr:
        if c.isdigit():
            num = num + c
    return num if num else 1

def clear_root_buttons(frame):
    for widgets in frame.winfo_children():
        if ('button' in str(widgets)):
            if (int(getnum(str(widgets)))>3):
                widgets.destroy() 

def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()