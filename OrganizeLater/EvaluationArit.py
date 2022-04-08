##a = int(input('Type in the the first number'))
##b = int(input('Type in the second number'))
##c = input('Type in / + - or *')
##if c == '/':
##    print(a / b)
##elif c == '+':
##    print (a+b)
##elif c == '-':
##    print(a-b)
##    
##elif c == '*':
##    print(a*b)
##else:
##    print('not a valid opperation')

##b = 'Arit'
##d = 'PasWoRd'
##a = input('Type in your username')
##if a == b:
##    c = input('What is the password (all letters)')
##    if c == d:
##        print('Correct')
##    else:
##        print('Wrong')
##else:
##    print('Not a valid username')
##

##for a in range(1,5):
##    for b in range(1,a+1):
##        print(a,end='')
##    print()

##a = None
##while a != 'Yes':
##    a = input('Do you want to quit? ')

##c = []
##f=[]
##b = [151,51,3,5,1,6,8,]
##for d in b:
##    if d % 2 != 0:
##        c.append(d*d*d)
##    else:
##       f.append(d*d) 
##        
##print(c)
##print(f)

##a = {'Apples':1, 'Bananas':2, 'Potatoes':0.8, 'Oranges':3}
####for b in a:
####    print(b,a[b])
##print(a.keys())

def ar(a):
    if a >= 500 and a < 1000:
        return 5
    elif a>=1000 and a < 1500:
        return 10
    elif a>=1500:
        return 15 
    else:
        return 0
print('You have a',ar(1000),'% discount!')
    
