from tkinter import *
import random
import pytz
from datetime import datetime
print(pytz.all_timezones)
root=Tk()
root.title("Frame")


#Frames
india_frame = Frame(root)
india_frame.grid(row=0, column = 0)

canada_frame = Frame(root)
canada_frame.grid(row=0, column = 1)

france_frame = Frame(root)
france_frame.grid(row=1, column = 0)

usa_frame = Frame(root)
usa_frame.grid(row=1, column = 1)

#Text Labels
india_text = Label(india_frame, text = "India")
india_text.pack(side = TOP)

india_timezone = pytz.timezone("Asia/Kolkata")
india_date = datetime.now(india_timezone) 
india_date = india_date.strftime("%Y-%m-%d %I:%M:%S %p %Z")
india_time = Label(india_frame, text= india_date)
india_time.pack(side = BOTTOM)

#Flags
india_flag = PhotoImage(file="IndiaFlag.png")
india_flag = india_flag.subsample(4,4)
india_flag_label = Label(india_frame,image = india_flag).pack()



while True:
    india_date = datetime.now(india_timezone) 
    india_date = india_date.strftime("%Y-%m-%d %I:%M:%S %p %Z")
    india_time["text"] = india_date

    root.update()