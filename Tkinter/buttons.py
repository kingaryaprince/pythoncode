from tkinter import *
import string
import random
password = ""
root=Tk()
root.title("Password Gen")
print(string.punctuation)
def Submit():

    password_strength = radio_variable.get()
    password_length = int(passlength.get())
    if password_strength == 1:
        new_password = random.sample(string.ascii_letters, password_length)
        new_password = ''.join(new_password)
        print(new_password)
    
    elif password_strength == 2:
        new_password = random.sample(string.ascii_letters+string.digits, password_length)
        new_password = ''.join(new_password)
        print(new_password)

    elif password_strength == 3:
        new_password = random.sample(string.ascii_letters+string.digits+string.punctuation, password_length)
        new_password = ''.join(new_password)
        print(new_password)
    pass_label["text"] = "Generated Password: " + new_password
#Label
pass_label = Label(root, text = "Generated Password: ")
pass_label.grid(row = 0, column = 0, columnspan= 5) 

strength_label = Label(root, text = "Password Strength")
strength_label.grid(row = 1, column = 0, columnspan= 2)

length_label = Label(root, text = "Password Length: ")
length_label.grid(row = 2, column = 0, columnspan= 2)



#Button
submit_button = Button(root, text = "Submit", bg = "green", fg = "white", command = Submit)
submit_button.grid(row = 3, column = 0, columnspan=5, pady=4, ipadx=10,ipady=5)


#Radio Button
radio_variable = IntVar()
low_button = Radiobutton(root, text = "Low", variable = radio_variable, value = 1)
medium_button = Radiobutton(root, text = "Medium", variable = radio_variable, value = 2)
high_button = Radiobutton(root, text = "High", variable = radio_variable, value = 3)

low_button.grid(row = 1, column = 2)
medium_button.grid(row = 1, column = 3)
high_button.grid(row = 1, column = 4)


passlength = Spinbox(root, from_=6, to = 12)
passlength.grid(row = 2, column = 2, columnspan=3)





root.mainloop()