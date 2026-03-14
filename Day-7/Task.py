products=["rice","sugar","wheatflour",'milk','eggs','cooking oil','tea powder','salt','Bread','soap']
prices=[60,30,40,20,70,80,110,35,45,65]
print("--------------------Welcome to groceery store--------------------")
print("Here are the available products \n")
print("Index".ljust(5," "),"Products".ljust(15," "),"prices".ljust(5," "))
for i in range(10):
    print(str(i+1).ljust(5," "),str(products[i]).ljust(15," "),str(prices[i]).ljust(5," "))
    
items=list(map(int, input(
    "Enter the indexs"
).split()))

print("Selected items:")
total=0
for item in items:
    print(str(products[item-1]).ljust(15," "),prices[item-1])
    total+= prices[item-1]
    
print("\n Total Amount: ",total)

""" 
def menu():
    print("------------Welcome to grocery shop-----------\n")
    print("Here are the list items available products: ")
    items={1:('Rice',60),2:('wheat Flour',45),3:('sugar',40),4:('Milk',25),5:("Eggs(12)",70),6:('Cooking oil',130),7:("Tea powder",90),8:("salt",20),9:("Bread",30),10:("soap",25)}
    print("No".ljust(5), "Item".ljust(15), "Price".rjust(5))
    print("-"*30)

    for key, value in items.items():
        name, price = value
        print(str(key).ljust(5), name.ljust(15), str(price).rjust(5))
    print("Pick the required items based upon the index numbers")

menu()
User_input=list(map(int , input("Enter the required items Indexs (eg 1 2 2 3 3 4 5 6 6 3 6 7)").split()))
"""