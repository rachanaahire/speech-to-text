
def clear_root_buttons(frame, s):
    for widgets in frame.winfo_children():
        print(widgets, s)
        if ('button' in str(widgets)):
            num = ""
            for c in str(widgets):
                if c.isdigit():
                    num = num + c
            print(num, type(num))
            if (num):
                if (int(num)>3):
                    widgets.destroy() 

def clear_frame(frame):
        for widgets in frame.winfo_children():
            widgets.destroy()