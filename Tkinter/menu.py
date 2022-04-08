from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

root = Tk()
root.title("Menu")
file_name = None

def new_function():
    global file_name
    textbox.delete("1.0",END)

def open_function():
    global file_name
    file_name = fd.askopenfilename()
    open_file = open(file_name, "r")
    text_file=open_file.read()
    textbox.insert("1.0", text_file)
    print("open")

def save_function():
    global file_name
    if file_name == None:
        file_name = fd.asksaveasfilename()
    save_file = open(file_name, "w")
    save_file.write(textbox.get("1.0", END))
    save_file.close()
    print("save")

def exit_function():
    root.destroy()

def about_function():
    mb.showinfo("Information", "Custom notepad") 

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "New", command = new_function)
filemenu.add_command(label = "Open", command = open_function)
filemenu.add_command(label = "Save", command = save_function)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit_function)
menubar.add_cascade(label = "File", menu = filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "About", command = about_function)
menubar.add_cascade(label = "Help", menu = helpmenu)
textbox = Text(root, height = 10, width = 20)
textbox.pack()
root.config(menu = menubar)

root.mainloop()

