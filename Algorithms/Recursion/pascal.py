print(1)
layer = [1, 1]
layers = 1


# while layers < 10:
#     for elem in layer:
#         print(elem,end=' ')
#     print()
    
#     new_layer = []
#     for i in range(len(layer)-1):
#         num1 = layer[i]
#         num2 = layer[i+1]
#         new_layer.append(num1 + num2)
#     new_layer=[1] + new_layer + [1]
#     layer=new_layer
#     layers+=1

def Pascal():
    global layer, layers
    if layers > 10:
        return
    for elem in layer:
        print(elem,end=' ')
    print()
    
    new_layer = []
    for i in range(len(layer)-1):
        num1 = layer[i]
        num2 = layer[i+1]
        new_layer.append(num1 + num2)
    new_layer=[1] + new_layer + [1]
    layer=new_layer
    layers += 1
    Pascal()

Pascal()