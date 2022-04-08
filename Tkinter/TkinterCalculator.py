from tkinter import *


root=Tk()
root.title("Calculator")

def clear():
    print("clear")
    entry.delete(0, END)

def equal():
    try:
        answer = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, answer)
    except Exception as E:
        print(E)
        entry.delete(0, END)
        entry.insert(END, "ERROR")
    
    

def click(char):
    entry.insert(END, char)


entry = Entry(root)
entry.grid(row = 0,column= 0, columnspan= 6)

#Other Buttons

clearbutton = Button(root, text = "C", command= clear, width = "3")
clearbutton.grid(row = 0, column = 6, columnspan=2, sticky= "NESW")

equalbutton = Button(root, text = "=", command = equal)
equalbutton.grid(row = 4, column = 4, columnspan=2, sticky= "NESW")

add = Button(root, text = "+", command= lambda:click('+'), width = "3")
add.grid(row = 1, column = 6, columnspan=2, sticky= "NESW")

sub = Button(root, text = "-", command= lambda:click('-'), width = "3")
sub.grid(row = 2, column = 6, columnspan=2, sticky= "NESW")

mul = Button(root, text = "*", command= lambda:click('*'), width = "3")
mul.grid(row = 3, column = 6, columnspan=2, sticky= "NESW")

div = Button(root, text = "/", command= lambda:click('/'), width = "3")
div.grid(row = 4, column = 6, columnspan=2, sticky= "NESW")

decimalbutton = Button(root, text = ".", command = lambda:click("."))
decimalbutton.grid(row = 4, column = 0, columnspan=2, sticky= "NESW")

#Number Buttons

num1 = Button(root, text = "1", command= lambda:click(1))
num1.grid(row = 1, column = 0, columnspan=2, sticky= "NESW")

num2 = Button(root, text = "2", command= lambda:click(2))
num2.grid(row = 1, column = 2, columnspan=2,sticky= "NESW")

num3 = Button(root, text = "3", command= lambda:click(3))
num3.grid(row = 1, column = 4, columnspan=2,sticky= "NESW")

num4 = Button(root, text = "4", command= lambda:click(4))
num4.grid(row = 2, column = 0, columnspan=2, sticky= "NESW")

num5 = Button(root, text = "5", command= lambda:click(5))
num5.grid(row = 2, column = 2, columnspan=2,sticky= "NESW")

num6 = Button(root, text = "6", command= lambda:click(6))
num6.grid(row = 2, column = 4, columnspan=2,sticky= "NESW")

num7 = Button(root, text = "7", command= lambda:click(7))
num7.grid(row = 3, column = 0, columnspan=2, sticky= "NESW")

num8 = Button(root, text = "8", command= lambda:click(8))
num8.grid(row = 3, column = 2, columnspan=2,sticky= "NESW")

num9 = Button(root, text = "9", command= lambda:click(9))
num9.grid(row = 3, column = 4, columnspan=2,sticky= "NESW")

num0 = Button(root, text = "0", command= lambda:click(0))
num0.grid(row = 4, column = 2, columnspan=2,sticky= "NESW")










root.mainloop()