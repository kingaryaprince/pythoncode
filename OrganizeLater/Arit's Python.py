##fruits = ['Apple', 'Banana', 'Orange']
##
##fruits[0] = 'Pear'
##x = sorted(fruits)
##print(fruits)
##
##'''sentance = "Hello,welcome,tosomewhere."
##s2 = list(sentance)
##s3 = "".join(s2)
##print (s3)'''
##import random
##list1 = []
##
##for x in range(1,100):
##   d = random.randint(1,1000)
##   list1.append(d)
##list1.sort()
##for s in range (1,len(list1)):
##
##    if list1[s] > 50:
##        print (list1[s])
##        print (list1)
##        break
##    else:
##        pass
##        
##
##import random
##list1 = ['Apple', 'Orange', 'Pinapple', 'Cheese', 'Fruit', 'Vegetable']
##word =  random.choice(list1)
##word1 = word
##scrambled =  list(word1)
##random.shuffle(scrambled)
##userchoice = input('What is this word?'+ "".join(scrambled))
##life = 5
##while life > 0:
##    userchoice = input('What is this word?'+ "".join(scrambled))
##    
##    if userchoice == word:
##        print('You win')
##        break
##    else:
##        life = life - 1
##        print('You didnt get it right yet. You have', life, ' lifves left')
##        
##
##if life == 0:
##    print ('you lose')
##        
##    
##import random
##list1 = ['Apple', 'Orange', 'Pinapple', 'Cheese', 'Fruit', 'Vegetable']
##randomchoice = random.choice(list1)
##
##randomchoice1 = list(randomchoice.lower())
##d = ['_'] * len(randomchoice)    
##print (d)
##
##while True:
##    f = input('Type in a letter: ')
##    f = f.lower()
##    if f in randomchoice1:
##        c = randomchoice1.index(f)
##        d[c] = f
##        print (d)
##        
##    if d == randomchoice1:
##        print('You win')
##        break
##    
##
##list1 = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'October', 'November', 'December']
##a=int(input('Pick a number below 12: '))
##d =list1[a-1]
##print(d)
##
##word = 'elephant'
##start = -1
##occ = 2
##for var in range (0,occ,1):
##   start = word.find('e', start + 1)
##print(start)
##ClassMark = [ 'Math', 'Writing','History','Science']
##
##BillMarks = [ 86 , 80 , 78 , 94 ]      #List
####
##TomMarks = [ 65 , 78 , 79 , 87 ]
####
##Mikemarks = [ 89 , 76 , 87 , 75 ]
##Li = [BillMarks, TomMarks, Mikemarks]
##print(ClassMark)
##for d in range(0,3,1):
##   print()
##   for i in range(0,4,1):
##      print(Li[d][i], end=' ')
## 
##d = (1,2,3)
##d = (1,3,5)
##b = d[0]
##c = d[1]
##e = d[2]
##d = ['a','a','b','a']
##print(d.count('
##import random
##d = []
##p = []
##for i in range(1,11,1):
##   a = random.randint(1,12)
##   if a % 2 == 0:
##      m = a * a
##      p.append(m)
##   else:
##      f = a ** 3
##      d.append(f)
##print(d)
##print(p)
##a = ['Hi', 'Bye']
##for d in a:
##   print(len(d))
##import random
##
##list1 = []
##for b in range(0,10):
##    a = random.randint(1,200)
##    list1.append(a)
##
##    if b == 5:
##        print()
##    print(a, end=" ")
####Ask the user to enter a number. Create an empty list and append all the numbers till that number in the list. Print half of the numbers in one line and the other half in another line.

####Write a program that has a list of 5 numbers of your choice. Create an empty list in the program. Double all the numbers in the first list and them to the second list.



##list1 = ['Bird', 'Dog', 'Cat', 'Lion', 'Fish']
##list2 = ['Caw', 'Bark', 'Meow', 'Roar', 'nothing']
##for d in range(0,5):
##    print(list1[d], list2[d])
##a = []
##user = int(input('Enter Numbers'))    
##for b in range(1,user+1,1):
##            a.append(b)
##    
##            
##                
##print(a[0:user//2])
##print(a[user//2:user])
##a = [1,2,3,4,5]
##c = []
##for b in a:
##    d = b + b
##    c.append(d)
##
##print(c)
##a = {'A':1,'B':2}
##for v in a:
##    print(a[v])
##    print(a.values()) 
##    
##print(a)
##a = {'Computer':100, 'Burger':4,'TV':600, 'Pineapple':3, 'Apple':2}
##for i in a:
##    print(i)
##userguess = input('What items do you want to buy?')
##if userguess in a:
##    print(a[userguess])
##    d = input('Do you want to buy it')
##    if d == 'yes':
##        print('Bought')
##        
##    elif d == 'no':
##        print('You didnt buy it')
##    else:
##        print('Yes or no')
##else:
##    print('Not in list')
##a = {'1+1':2, '2^3':8,'2+2':4,'3+3':6, '4*4':16}
##for r in a:
##    b = int(input(r))
##    if b == a[r]:
##        print('Correct')
##    else:
##        print('Wrong')
##a= {1:'',2:'',3:'',4:'',5:''}
##for f in a:
##    a[f] = f * f
##print(a)

