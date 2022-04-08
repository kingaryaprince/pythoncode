x = "   Good   Morning   "
y = x.strip()
print(y)



##def pattern(x=10,y=5):
##    for z in range(1,x+1,1):
##        print()
##        for w in range(1,y+1,1):
##            print("*", end=" ")
##pattern()



##x = 6
##def change():
##    global x
##    x = 7
##change()
##print(x)



##import Calculator
##userfunction = input("Choose +  -  *  /  :  ")
##a = int(input("Pick your first number: "))
##b = int(input("Pick your second number: "))
##if userfunction == "+":
##    answer = Calculator.addfunc(a,b)
##    print(answer)
##elif userfunction == "-":
##    answer = Calculator.subtractfunc(a,b)
##    print(answer)
##elif userfunction == "*":
##    answer = Calculator.multiplyfunc(a,b)
##    print(answer)
##elif userfunction == "/":
##    answer = Calculator.dividefunc(a,b)
##    print(answer)
##




##def addfunc(x,y):
##    return x+y
##def subtractfunc(x,y):
##    return x-y
##def multiplyfunc(x,y):
##    return x*y
##def dividefunc(x,y):
##    return x/y
##userfunction = input("Choose +  -  *  /  :  ")
##a = int(input("Pick your first number: "))
##b = int(input("Pick your second number: "))
##if userfunction == "+":
##    answer = addfunc(a,b)
##    print(answer)
##elif userfunction == "-":
##    answer = subtractfunc(a,b)
##    print(answer)
##elif userfunction == "*":
##    answer = multiplyfunc(a,b)
##    print(answer)
##elif userfunction == "/":
##    answer = dividefunc(a,b)
##    print(answer)

###Class Star Feb6####



##def reversedstring(x):
##    new=""
##    for y in range(len(x)-1,-1,-1):
##        new=new+x[y]
##    print(new)
##    print(x)
##reversedstring("hello")


##
##def calculator(w,x,y,z):
##    print((w+x+y+z)/4)
##calculator(5,9,6,4)
##a,b,c,d = 10,2,4,8
##calculator(a,b,c,d)   




###TICTACTOE##

##winner = ""
##TTT = {}
##turn = 1
##for x in range(1, 10, 1):
##    TTT[x] = "_"
##print(TTT)
##
##while True:
##    for x in TTT:
##        print(TTT[x], end = " ")
##        if x%3 == 0:
##            print()
##    for z in range(1,4,1):
##        if TTT[z] == TTT[z+3] == TTT[z+6]:
##            winner = TTT[z]
##            break
##    for z in range(1,8,3):
##        if TTT[z] == TTT[z+1]== TTT[z+2]:
##            winner = TTT[z]
##            break
##    if TTT[1] == TTT[5] == TTT[9] or TTT[3] == TTT[5] == TTT[7]:
##        winner=TTT[5]
##    if winner == "X":
##        print("Player X won")
##        break
##    elif winner == "O":
##        print("Player O won")
##        break
##    elif turn == 10:
##        print("It's a draw")
##        break
##    sqr_num = int(input("Enter a square number: "))
##    if sqr_num not in range(1,10,1):
##        print("Choose a number between 1 and 9")
##        continue
##    if turn%2 == 0 and TTT[sqr_num] == "_":
##        TTT[sqr_num] = "O"
##        turn += 1
##    elif TTT[sqr_num] == "_":
##        TTT[sqr_num] = "X"
##        turn+=1    
    
    
    



##ListGrade = []
##Grade = {"Student1":93, "Student2":89, "Student3":99}
##for x in Grade:
##    Grade[x] = Grade[x] + 5
##    print(Grade)
##    if 100<Grade[x]:
##        Grade[x] = "A+"
##    elif 90<Grade[x]<=100:
##        Grade[x] = "A"
##        ListGrade.append(x)
##    elif 80<Grade[x]<=90:
##         Grade[x] = "B"
##for y in ListGrade:
##    del Grade[y]
##print(Grade)




##Grade = {"Student1":93, "Student2":89, "Student3":99}
##for x in Grade:
##    Grade[x] = Grade[x] + 5
##    print(Grade)
##    if 100<Grade[x]:
##        Grade[x] = "A+"
##    elif 90<Grade[x]<=100:
##        Grade[x] = "A"
##    elif 80<Grade[x]<=90:
##         Grade[x] = "B" 
##print(Grade)




##Class Start Jan 15##


##Questions = ["What is 1+1", "What is 1+2", "What is 1+3"]
##Answers = [2,3,4]
##Dictionary = {}
##for x in range(0,len(Questions),1):
##    Dictionary[Questions[x]] = Answers[x]
##print(Dictionary)
    



##word = input("Type a word: ")
##Dictionary = {}
##for x in word:
##    Dictionary[x] = word.find(x)
##print(Dictionary)



##Numbers = {1:"", 2:"",3:"",4:"",5:""}
##for x in Numbers:
##    Numbers[x] = x*x
##print(Numbers)
##



##Question = {"What is 2 + 2" : 4, "What is 10 + 11": 21, "What is 16 * 2": 32}
##for x in Question:
##    print(x)
##    answer = int(input(": "))
##    if answer ==  Question[x]:
##        print("That's correct!")
##    else:
##        print("That's wrong :C")




##GrocceryPrice = {"Apple":0.50, "Banana": 0.75, "Milk": 4}
##print(list(GrocceryPrice.keys()))
##item = input("What item do you want: ")
##if item in GrocceryPrice:
##    print(GrocceryPrice[item])



##Dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"}
##del Dictionary["key1"] ##How to delete from dictionary##
##print(Dictionary.values())



##Dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"}
##Dictionary["key1"] = "value4" ##This is how to replace Dictionary, if you use same key, it replaces value
##print(Dictionary)




#Dictionary Lesson Started

##L = ["word", "car", "truck", "sentence", "comma", "paragraph"]
##L2 = []
##for x in L:
##    length = len(x)
##    L2.append(length)
##print(L2)
##    



###Class Start Jan 9



##x=1
##L = [1,3,2,7,14,17,12,9,21]
##length = len(L)//2
##while True:
##    L.pop(x)
##    print(x)
##    print(L)
##    x=x+1
##    if length == x:
##        L.pop(x)
##        print(x)
##        print(L)
##        break
##print(L)


##import random
##L = ["word", "sentence", "paragraph", "period", "comma"]
##answer = random.choice(L)
##wordlist = (list(answer))
##random.shuffle(wordlist)
##print(wordlist)
##guess = input("Guess the word: ")
##if guess == answer:
##    print("You were correct")
##else:
##    print("You were wrong")



##L = ["word", "sentence", "paragraph", "period", "comma"]
##user = input("Type a letter: ")
##for x in L:
##    if user in x:
##        print(user)
##        print(x.find(user))
    



#tuples cannot be changed



##person1=[86, 80, 78]
##person2=[65,78,79]
##person3=[89,76,87]
##total = [person1, person2, person3]
##for x in total:
##    print(x)

