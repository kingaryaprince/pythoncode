from tkinter import *
Grocery = {"Milk": 2,"Chocolates": 3,"Eggs": 4,"Bread": 5,"Fruits": 6}
SelectedItems = []
Checkout = {}

root=Tk()
root.title("Grocery Price Calculator")


check_milk = IntVar()
check_chocolates = IntVar()
check_eggs = IntVar()
check_bread = IntVar()
check_fruits = IntVar()

check_milk.set(0)
check_chocolates.set(0)
check_eggs.set(0)
check_bread.set(0)
check_fruits.set(0)


frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame3 = Frame(root)
def clear():
    milk_button.deselect()
    chocolates_button.deselect()
    eggs_button.deselect()
    bread_button.deselect()
    fruits_button.deselect()

def next1():
    r = 0
    global Checkout
    frame1.pack_forget( )
    frame2.pack()
 
    if check_milk.get() == 1:
        SelectedItems.append("Milk")
    if check_chocolates.get() == 1:
        SelectedItems.append("Chocolates")
    if check_eggs.get() == 1:
        SelectedItems.append("Eggs")
    if check_bread.get() == 1:
        SelectedItems.append("Bread")
    if check_fruits.get() == 1:
        SelectedItems.append("Fruits")
    print(Checkout)
    for x in SelectedItems: 
        spin_val = Spinbox(frame2, from_=0,  to= 10)
        spin_val.grid(row=r, column=2)
        Checkout[x] = spin_val
        food_label = Label(frame2,text = x)
        food_label.grid(row = r, column = 0)
        r+=1
        print(Checkout)
    
    checkout_button = Button(frame2, text = "Checkout", command = checkout)
    checkout_button.grid(row = r, column=2)

def checkout():
    r = 1
    frame2.pack_forget( )
    frame3.pack()
    #Labels
    items_label = Label(frame3,text = "Items")
    items_label.grid(row = 0, column = 0)

    quantity_label = Label(frame3,text = "Quantity")
    quantity_label.grid(row = 0, column = 1)

    unitprice_label = Label(frame3,text = "Unit Price")
    unitprice_label.grid(row = 0, column = 2)

    total_label = Label(frame3,text = "Total")
    total_label.grid(row = 0, column = 3)
    for x in Checkout:
        label = Label(frame3, text = x)
        label.grid(row = r, column = 0)

        label = Label(frame3, text = Checkout[x].get() )
        label.grid(row = r, column = 1)

        label = Label(frame3, text = "$" + str(Grocery[x]) )
        label.grid(row = r, column = 2)

        label = Label(frame3, text = "$"+str(Grocery[x]*int(Checkout[x].get())))
        label.grid(row = r, column = 3)
        r+=1
    


#Label
text1_label = Label(frame1,text = "Choose the items you want to buy")
text1_label.grid(row = 0, column = 0,columnspan=4) 

#Entry Box
#user_entry = Entry(root)
#user_entry.grid(row = 0, column = 1) 

#Button
clear_button = Button(frame1, text = "Clear", command = clear)
clear_button.grid(row = 6, column=0)
next1_button = Button(frame1, text = "Next", command = next1)
next1_button.grid(row = 6, column=2 )

milk_button = Checkbutton(frame1, text = "Milk", variable = check_milk)
chocolates_button = Checkbutton(frame1, text = "Chocolates", variable = check_chocolates)
eggs_button = Checkbutton(frame1, text = "Eggs", variable = check_eggs)
bread_button = Checkbutton(frame1, text = "Bread", variable = check_bread)
fruits_button = Checkbutton(frame1, text = "Fruit", variable = check_fruits)

milk_button.grid(row = 1, column = 1,sticky= 'w') 
chocolates_button.grid(row = 2, column = 1,sticky= 'w') 
eggs_button.grid(row = 3, column = 1,sticky= 'w') 
bread_button.grid(row = 4, column = 1,sticky= 'w') 
fruits_button.grid(row = 5, column = 1,sticky= 'w') 


    



root.mainloop()