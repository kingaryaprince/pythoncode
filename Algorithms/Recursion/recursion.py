import time
num1 = 0
num2 = 1
sum = 0
series_len = 100
count = 0
start = time.time()
def Fibonacci():
    
    global num1, num2, count
    print(num1)

    sum = num1+num2
    num1 = num2
    num2 = sum
    count += 1
    if count > series_len:
        stop = time.time()
        print(stop-start)
        return
    Fibonacci()

Fibonacci()
