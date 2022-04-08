NumList = [9,7,3,4,10, 99,2,312,423,0,23]
check = 0
min = 0
leastVal = 0
count = 0
val = 0
while True:
    for x in range(val, len(NumList)):
        check = 0
        if NumList[x] < NumList[leastVal]:
            print(NumList)
            check = 1
            leastVal = x
            print(NumList[leastVal])
            
    NumList[min], NumList[leastVal] = NumList[leastVal], NumList[min]
    print(NumList)
    min+=1
    val +=1
            
    print(NumList)

    if val == 10:
        break
