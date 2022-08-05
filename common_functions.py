
def getnum(mystr):
    num = ""
    for c in mystr:
        if c.isdigit():
            num = num + c
    return num if num else 1

def clear_root_buttons(frame):
    for widgets in frame.winfo_children():
        wid = str(widgets)
        if ('button' in wid):
            if (int(getnum(wid))>3):
                widgets.destroy() 
        if ('label' in wid):
            if (int(getnum(wid))>2):
                widgets.destroy() 

def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()