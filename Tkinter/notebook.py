
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Notebook")

notebook = ttk.Notebook(root)
frame1 = Frame(notebook)
notebook.add(frame1, text = "Frame 1")

frame2 = Frame(notebook)
notebook.add(frame2, text = "Frame 2")
notebook.pack()

notebook.pack()



root.mainloop()
