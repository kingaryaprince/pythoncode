from tkinter import *

root = Tk()
root.title("Quiz Game")

qnum = 0
score = IntVar()

class Question():
    def __init__(self, question, options, answer, answer_index):
        self.question = question
        self.options = options
        self.answer = answer
        self.answer_index = answer_index


question1 = Question("What is 2 + 2?", ["2", "3", "4", "5"], "4", 2)
question2 = Question("What color is an apple usually?", [
                     "Red", "Green", "Purple", "Blue"], "Red", 0)
question3 = Question("What is 7 + 3?", ["27", "10", "6", "13"], "10", 1)

question_list = [question1, question2, question3]
option_list = []

x = question_list[qnum].question


def submit():
    global option_list, qnum, score
    if answer.get() == question_list[qnum].answer:
        option_list[question_list[qnum].answer_index].configure(fg='green')
        print("correct")
        score.set(score.get()+1)
    else:
        for x in range(len(question_list[qnum].options)):
            if question_list[qnum].options[x] == answer.get():
                option_list[x].configure(fg='red')
                print(option_list[x])
        option_list[question_list[qnum].answer_index].configure(fg='green')
        print("wrong")
        score.set(score.get()-1)


def next_frame():
    global qnum, x, question_label, option_list
    qnum += 1
    if qnum == len(question_list):
        exit()
    x = question_list[qnum].question

    question_label.pack_forget()
    for opt in option_list:
        opt.pack_forget()

    question_label = Label(frame2, text=x)
    question_label.pack()

    answer.set(None)

    option_list = []
    for y in question_list[qnum].options:
        option = Radiobutton(frame2, variable=answer, text=y, value=y)
        option_list.append(option)
        option.pack()



frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame1.pack()
frame2.pack()
frame3.pack()


# Label
score_label = Label(frame1, textvariable = score)
score_label.grid(row=0, column=0, columnspan=4)

question_label = Label(frame2, text=x)
question_label.pack()

answer = StringVar()
answer.set(None)

for x in question_list[qnum].options:
    option = Radiobutton(frame2, variable=answer, text=x, value=x)
    option_list.append(option)
    option.pack()


# Entry Box
#user_entry = Entry(root)
#user_entry.grid(row = 0, column = 1)


# Button
submit_button = Button(frame3, text="Submit", command=submit)
submit_button.grid(row=6, column=0)

next_button = Button(frame3, text="Next", command=next_frame)
next_button.grid(row=6, column=4)


root.mainloop()

#
