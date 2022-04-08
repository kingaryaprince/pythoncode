NumList = [9,7,3,4,10, 99,2,312,423,0,23]
check = -1

# while True:
#     check = 0
#     for x in range(len(NumList)):

#         if x == len(NumList)-1:
#             break

#         if NumList[x]>NumList[x+1]:
#             NumList[x], NumList[x+1] = NumList[x+1], NumList[x]
#             check = 1
#         print(NumList)
#     if check == 0:
#         break


def RecursiveBubble():
    global NumList, check

    if check == 0:
        return

    check = 0

    for x in range(len(NumList)-1):
        if NumList[x] > NumList[x+1]:
            NumList[x], NumList[x+1] = NumList[x+1], NumList[x]
            check = 1
        print(NumList)

    RecursiveBubble()

RecursiveBubble()