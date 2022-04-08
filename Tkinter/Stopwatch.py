from tkinter import *
import time
root=Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
timer = StringVar()
timer.set("00:00:00")
label = Label(root, textvariable= timer)
label.grid(row = 0, column = 0, columnspan=3)
s = 0
m = 0
h = 0
current_time = 0
started = False

def Start():
    global current_time
    global started
    if started == False:
        started = True
        current_time = root.after(200,increaseTimer)
    

def Stop():
    global started 
    root.after_cancel(current_time)
    started = False

def Reset():
    global s, m, h
    s = 0
    m = 0
    h = 0
    timer.set("00:00:00")
keyboard=Frame(root)
keyboard.grid(row=1,column=0, sticky=NSEW)
keyboard.grid_rowconfigure(0, weight=1)
keyboard.grid_columnconfigure(0, weight=1)


start_button = Button(keyboard, padx=5, pady=5, text="Start",command=Start, bg = "green", fg = "white")
start_button.grid(row=0, column=0, sticky='EWNS')

keyboard.grid_columnconfigure(1, weight=1)
stop_button = Button(keyboard, padx=5, pady=5, text="Stop",command=Stop, bg = "red", fg = "white")
stop_button.grid(row=0, column=1, sticky='EWNS')


keyboard.grid_columnconfigure(2, weight=1)
reset_button =Button(keyboard, padx=5, pady=5, text="Reset",command=Reset, bg = "blue", fg = "white")
reset_button.grid(row=0, column=2, sticky='EWNS')



def increaseTimer():
    global s, m, h, current_time
    s += 1
    if s == 60:
        m += 1
        s = 0
    
    if m == 60:
        h += 1
        m = 0
    
    timer.set(str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2))
    current_time=root.after(200, increaseTimer)

root.mainloop()
