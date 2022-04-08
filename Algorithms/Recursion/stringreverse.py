str1 = "best"
str2 = ""
num= 1
def revString():
    global num, str1, str2
    if len(str2) == len(str1):
        return
    length = len(str1)
    #print(str1[length-1])
    str2 = str2 + str1[length-num]
    num +=1
    print(str2)
    revString()

revString()