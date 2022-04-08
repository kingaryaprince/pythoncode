from tkinter import *
import random

root=Tk()
root.title("Color Game")
score = 0
color_word = "black"
color = "black"
colors = ["red","blue","orange","yellow","green","pink","purple"]

color = random.choice(colors)
color_word = random.choice(colors)

def Submit():
    print("Submit")
    global color, color_word, score
    if entry.get() == color:
        score +=1
        color = random.choice(colors)
        color_word = random.choice(colors)
    else:
        color = random.choice(colors)
        color_word = random.choice(colors)
    score_label["text"] = "Score: "+ str(score)
    color_label["text"] = str(color_word)
    color_label["fg"] = str(color)
    root.update()   


score_label = Label(root, text = "Score: " + str(score), font = ("Arial","15", "bold"))
score_label.grid(row = 0, column = 1) 

text_label = Label(root, text = "Type the color of the word shown below", font = ("Arial","15", "bold"))
text_label.grid(row = 1, column = 0, columnspan=3) 

color_label = Label(root, text = color_word, fg = color, font = ("Arial","15", "bold"))
color_label.grid(row = 2, column = 0, columnspan=3) 

entry = Entry(root,font = ("Arial","15", "bold"))
entry.grid(row = 3, column = 0, columnspan=3) 

submit_button = Button(root, text = "Submit", fg = "white", bg = "green", command = Submit,font = ("Arial","15", "bold"))
submit_button.grid(row = 4, column = 1, sticky = N+E+S+W)





root.mainloop()
