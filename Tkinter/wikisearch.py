from tkinter import *
import wikipedia

root = Tk()
root.title("Wiki Search")
def submit():
    textbox.delete("1.0", END)
    info = wikipedia.summary(entry.get(), sentences = 1)
    textbox.insert(END, info)



label = Label(root, text = "Search")
label.pack()    
entry = Entry(root)
entry.pack()
button = Button(root, text = "Submit", command = submit)
button.pack()



textbox = Text(root)
textbox.pack()

root.mainloop()