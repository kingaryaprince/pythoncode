from tkinter import *


root = Tk()
root.title("Option")
var = StringVar()
Month = [i for i in range(1,13)]
Day = [i for i in range(1,32)]
Year = [i for i in range(2000,2022)]

print(Month, Day, Year)
dropdown = OptionMenu(root, var, *Month)
dropdown.grid(row = 1, column= 1, columnspan=4)
value = var.get()
root.mainloop()