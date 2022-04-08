
from abc import abstractmethod
from tkinter import *
from tkinter import font
import random
import time
root=Tk()
root.title("Calculator")
click1 = None
click2 = None
clickcount = 1
timecount = 0

finish_indicator = 0

def update_timer():
    global timecount
    if finish_indicator == 8:
        timer["text"] = "Finished. Your score is: " +str(timecount)
    else:
        timecount += 1
        timer["text"] = "Time: " +str(timecount)
        global roottimer
        roottimer = root.after(1000,update_timer)
    


def clear(index, match):
    if not match:
        ButtonList[index]["text"] = "?"
    


def click(index):

    global click1, finish_indicator, clickcount

    #Changes text on button to number and back
    if click1 != index:
        
        
        if ButtonList[index]["text"] == "?":
            ButtonList[index]["text"] = NumberList[index]
        else:
            return

        clickcount+=1
        match = False

        if clickcount <= 2:
            print("count <= 2")

        else:
            clickcount = 1
            #time.sleep(2)
        

        if click1 is not None:
            if NumberList[click1] == NumberList[index]:
                ButtonList[index]["text"] = NumberList[index]
                ButtonList[click1]["text"] = NumberList[click1]
                match = True
                finish_indicator += 1
                root.update()
                print("match", click1, index, finish_indicator)


            else:
                match = False
                #ButtonList[index]["text"] = NumberList[index]
                print("not match")
                root.update()
                time.sleep(.2)
                clear(index,match)
        else:
            root.update()
            time.sleep(.2)
            clear(index,match)
        #root.after(1500, lambda:clear(index, match))
        
        print(clickcount)
            
        
        click1 = index

    #if match == 0:
        
    #else:
    #    print("Match")
#Other Buttons

#decimalbutton = Button(root, text = ".", command = lambda:click("."))
#decimalbutton.grid(row = 4, column = 0, columnspan=2, sticky= "NESW")

#Number Buttons

ButtonList = []
NumberList = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
random.shuffle(NumberList)
indexcount = 0
#num1 = Button(root, text = "1", command= lambda:click(1))
#num1.grid(row = 1, column = 0, columnspan=2, sticky= "NESW")




ButtonFont = font.Font(size = 40)

for x in range(4):
    for y in range(4):
        button = Button(root, text = "?", font = ButtonFont, command = lambda i = indexcount:click(i), width=6,height=3)
        ButtonList.append(button)
        button.grid(row = x, column = y)
        indexcount += 1

timer = Label(root, text = "Time: 0", font = ("Ariel",20))
timer.grid(row = 5, column = 1, columnspan=2)
print(NumberList)
print(ButtonList)






update_timer()
root.mainloop()