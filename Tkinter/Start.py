# from tkinter import *
# root=Tk()
# root.title("First Tkinter")

# def clear():
#     name_entry.delete(0, END)

# def submit():
#     a = name_entry.get()
#     print(a)
# #Label
# name_label = Label(root, text = "Name")
# name_label.pack() 

# #Entry Box
# name_entry = Entry(root)
# name_entry.pack()

# #Button
# exit_button = Button(root, text = "Exit", fg = "red", command = exit)
# exit_button.pack()

# clear_button = Button(root, text = "Clear", fg = "blue", command = clear)
# clear_button.pack()

# submit_button = Button(root, text = "Submit", fg = "green", command = submit)
# submit_button.pack()

# root.mainloop()

# from tkinter import *
# root=Tk()
# root.title("First Tkinter")

# def clear():
#     name_entry.delete(0, END)

# def submit():
#     a = name_entry.get()
#     print(a)
# #Label
# name_label = Label(root, text = "Name")
# name_label.grid(row = 0, column = 0) 

# food_label = Label(root, text = "Food")
# food_label.grid(row = 1, column = 0) 

# title_label = Label(root, text = "Please fill out form")
# title_label.grid(row = 3, column = 0, columnspan = 2) 
# #Entry Box
# name_entry = Entry(root)
# name_entry.grid(row = 0, column = 1)

# food_entry = Entry(root)
# food_entry.grid(row = 1, column = 1)
# #Button
# exit_button = Button(root, text = "Exit", fg = "red", command = exit)
# exit_button.grid(row = 2, column = 0    )

# submit_button = Button(root, text = "Submit", fg = "green", command = submit)
# submit_button.grid(row = 2, column = 1)


# root.mainloop()




# from tkinter import *
# root=Tk()
# root.title("First Tkinter")

# #Label
# a, b = "black", "white" 

# for x in range(0,8):
#     a,b = b,a
#     for y in range(0,8):
#         name_label = Label(root, width = 3, bg = a)
#         name_label.grid(row = x, column = y) 
#         a,b = b,a


# from tkinter import *
# root=Tk()
# root.title("Temp Converter")

# def clear():
#     f_entry.delete(0, END)

# def calculate():
#     a = f_entry.get()
#     a = (int(a)-32)*(5/9)
#     c_entry.insert(0, a)
# #Label
# f_label = Label(root, text = "Fahrenheit")
# f_label.grid(row = 0, column = 0) 

# c_label = Label(root, text = "Celsius")
# c_label.grid(row = 0, column = 1) 

# #Entry Box
# f_entry = Entry(root)
# f_entry.grid(row = 1, column = 0) 

# c_entry = Entry(root)
# c_entry.grid(row = 1, column = 1) 



# #Button
# clear_button = Button(root, text = "Clear", fg = "blue", command = clear)
# clear_button.grid(row = 2, column = 0, sticky = N+E+S+W) 

# calculate_button = Button(root, text = "Calculate", fg = "green", command = calculate)
# calculate_button.grid(row = 2, column = 1, sticky = N+E+S+W) 

# root.mainloop()


''' Social Media Login '''

'''
from tkinter import *
import webbrowser

root=Tk()
root.title("Social Media")
value = None
def goTo(browser, username):
    webbrowser.open_new_tab(browser)
    label["text"] = username
#Label
label = Label(root, text = "Username")
label.grid(row = 2, column = 0, columnspan = 2) 




#Button
fb_button = Button(root, text = "Facebook", bg = "blue", fg = "white", command = lambda:goTo("www.facebook.com", "1"))
fb_button.grid(row = 0, column = 0, sticky = N+E+S+W)

ig_button = Button(root, text = "Instagram", bg = "red", fg = "white", command = lambda:goTo("www.instagram.com", "2"))
ig_button.grid(row = 0, column = 1, sticky = N+E+S+W)

t_button = Button(root, text = "Twitter", bg = "green", fg = "white", command = lambda:goTo("www.twitter.com", "3"))
t_button.grid(row = 1, column = 0, sticky = N+E+S+W) 

sc_button = Button(root, text = "Snapchat", bg = "yellow", fg = "white", command = lambda:goTo("www.snapchat.com", "4"))
sc_button.grid(row = 1, column = 1, sticky = N+E+S+W) 


root.mainloop()
'''


