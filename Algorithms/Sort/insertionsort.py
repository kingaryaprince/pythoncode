dif = 1
NumList = [9,7,3,4,10,19,2,3,20,5]
print(len(NumList))
length = len(NumList)
print(length)
# for x in range(1, length):
#     dif=1
#     if NumList[x]<NumList[x-dif]:
#         var = NumList[x]<NumList[x-dif]
#         while var:
#             print(dif)
#             NumList.insert(x-dif,NumList[x])
#             NumList.pop(x+1)
#             print(NumList)
#             dif+=1
print(NumList[1],NumList[0])

for x in range(1, length):
    print(NumList)
    move = x-1
    while NumList[x]<NumList[move]:
        print (NumList[x],NumList[move])
        if move == 0:
            break
        move = move-1

    if NumList[x]>NumList[move]:
        move+=1
        
    val = NumList.pop(x)
    NumList.insert(move, val)
    print(NumList)



        


