numlist = [1,21,92,3,25,5,78,2,100]
numlist.sort()
print(numlist)
x = 5

min_index = 0
max_index = len(numlist)
mid_index = (min_index+max_index)//2

while True:
    if x == numlist[mid_index]:
        print(mid_index, numlist[mid_index])
        
    if x > numlist[mid_index]:
        min_index=mid_index+1
        mid_index = (min_index+max_index)//2
        print("min", numlist[min_index], numlist[mid_index], numlist[max_index])
        

    if x< numlist[mid_index]:
        max_index = mid_index-1
        mid_index = (min_index+max_index)//2
        print("max", numlist[min_index], numlist[mid_index], numlist[max_index])
    
    
    if min_index > max_index:
        print("mid_index")
