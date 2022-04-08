from tkinter import *
from tkinter import messagebox
import webbrowser

users = {"aryap":"1234", "princearya":"arya", "prince":"king"}


root=Tk()
root.title("Login")
show = IntVar()
show.set(0)
value = None
def login():
    if user_entry.get() in users:
        if pass_entry.get() == users[user_entry.get()]:
            messagebox.showinfo("Success", "You have logged in")
        else:
            messagebox.showwarning("Wrong Password", "Wrong password entered")
        
    else:
        messagebox.showerror("Error", "User not found")

def clear():
    print("clear")

def show_pass():
    if show.get() == 1:
        pass_entry.configure(show = "")
    else:
        pass_entry.configure(show = "*")

#Label
user_label = Label(root, text = "Username")
user_label.grid(row = 0, column = 0) 

pass_label = Label(root, text = "Password")
pass_label.grid(row = 1, column = 0) 

#Entry Box
user_entry = Entry(root)
user_entry.grid(row = 0, column = 1) 

pass_entry = Entry(root, show = "*")
pass_entry.grid(row = 1, column = 1) 

#Button
login_button = Button(root, text = "Login", bg = "green", fg = "white", command = login)
login_button.grid(row = 3, column = 0, sticky = N+E+S+W)

clear_button = Button(root, text = "Clear", bg = "blue", fg = "white", command = clear)
clear_button.grid(row = 3, column = 1, sticky = N+E+S+W)

show_button = Checkbutton(root, text = "Show Password", variable = show, command= show_pass)
show_button.grid(row=2, column= 0)



root.mainloop()