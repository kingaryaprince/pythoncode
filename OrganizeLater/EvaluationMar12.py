##import time
##x = 0
##y = 1
##while True:
##    x = x+y
##    print(x)
##    time.sleep(0.25)
##    if x ==10 or x ==0:
##        y = -y
##    
## 

##codes = {"a":10, "ab":20, "abc":25, "abcd":50}
##spent = int(input("How much did you spend: ")) #More than 100 = 10 percent discount, 200 = 20 percent, 250 = 25 percent
##if 200 > spent > 100:
##    print("You get a 10% discount!")
##elif 250 > spent > 200:
##    print("You get a 20% discount!")
##elif spent > 250:
##    print("You get a 25% discount!")
##    question = input("Do you have a discount code [Type Yes or No]: ")
##    if question == "Yes":
##        code = input("Enter code: ")
##        code = code.lower()
##        code = code.strip()
##        if code in codes:
##            print(code)
##            print("You get a", codes[code], "percent discount!")
##            del codes[code]
##        else:
##            print("Invalid")\
##
##import random
##Dictionary = {}
##with open("names.txt", "r") as names:
##    for x in names:
##        y = x.strip()
##        a,b = y.split()
##        Dictionary[a+"."+b] = str(random.randint(1000,9999))
##        print(Dictionary)



