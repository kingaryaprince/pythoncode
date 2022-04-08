num = [1,2,3,4,5,6,7,8,9,4,4,4,4]
var = 4
index = []
found = False
for x in range(len(num)):
    if num[x] == var:
        found = True
        index.append(x)

if found == True:
    print(var)
    print(index)
else:
    print("Number not found")