from tkinter import *
root=Tk()
root.title("Word Shuffle Game")
import requests
import random
start_text = "Click To Start"
words = requests.get("http://random-word-api.herokuapp.com/word?number=20")
wordList = eval(words.text)
print(wordList, type(wordList))
word = ""
shuffle_word = ""
score = 0
x = 0
def Start():
    global word
    global shuffle_word
    global x
    if word == "":  
        start_button["text"] = "Guess the scrambled word"
        word = wordList[x]
        shuffle_word = list(word)
        random.shuffle(shuffle_word)
        shuffle_word = "".join(shuffle_word)
        print(word, shuffle_word)
        label["text"]= shuffle_word
    
def Submit():
    global score
    global word
    global x
    if entry.get() == word:
        entry.delete(0,END)
        score +=1
        x +=1
        word = wordList[x]
        shuffle_word = list(word)
        random.shuffle(shuffle_word)
        shuffle_word = "".join(shuffle_word)
        print(word, shuffle_word)
        label["text"]= shuffle_word
        score_label["text"] = score

entry = Entry(root)
entry.grid(row = 1, column = 1) 

label = Label(root, text = word)
label.grid(row = 1, column = 0) 

score_label = Label(root, text = "")
score_label.grid(row = 2, column = 0) 


start_button = Button(root, text = start_text, fg = "black", bg = "orange", command = Start)
start_button.grid(row = 0, column = 0, sticky = N+E+S+W, columnspan = 2) 

submit_button = Button(root, text = "Submit", fg = "white", bg = "green", command = Submit)
submit_button.grid(row = 2, column = 1, sticky = N+E+S+W) 

root.mainloop()
