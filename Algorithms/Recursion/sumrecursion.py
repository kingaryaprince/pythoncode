num = 132123
val1 = 0
val2 = 0
valsum = 0
def sumDigits():
    global val1, val2, valsum, num
    if num == 0:
        print("Reached end")
        return
    val1 = num%10
    num = num//10
    
    valsum = valsum +val1
    print(val1, valsum)

    print("val1 =" + str(val1), "num = " +str(num), "valsum = " +str(valsum))
    
    sumDigits()
    
sumDigits()