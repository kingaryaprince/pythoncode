from tkinter import *
import random

root=Tk()
root.title("Color Game")
score = 0
color_word = "black"
color = IntVar()



text_label = Label(root, text = "Type the color of the word shown below", font = ("Arial","15", "bold"))
text_label.grid(row = 1, column = 0, columnspan=3) 

color_scale = Scale(root, label = "Color", variable=color, from_=0, to=255, orient=VERTICAL)
color_scale.grid(row = 0, column = 0)



root.mainloop()
