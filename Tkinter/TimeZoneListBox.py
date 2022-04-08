from tkinter import *
import random
import pytz
from datetime import datetime
print(pytz.all_timezones)
root=Tk()
root.title("Frame")

TimezoneList = pytz.all_timezones

text1 = Label(root, text = "Choose any Timezone")
text1.grid(row = 0, column = 1)

text2 = Label(root, text = "Time")
text2.grid(row = 2, column = 1)

listbox = Listbox(root)
listbox.grid(row = 1, column=1)

for timezone in TimezoneList:
    listbox.insert(END, timezone)
selection = listbox.curselection()
   
index = 0

while True:
    selection = listbox.curselection()
    if len(selection) > 0: 
        index = selection[0]
    india_timezone = pytz.timezone(listbox.get(index))
    india_date = datetime.now(india_timezone) 
    india_date = india_date.strftime("%Y-%m-%d %I:%M:%S %p %Z")
    text2["text"] = india_date
    root.update()

root.mainloop()



    #selection = listbox.curselection()
    #print(selection)
    #index = selection[0]
    