# For loop is used to iterate the sequence items(list or tuple or number etc...)

# Examples for loop

products=["laptop","Mobile","Tablet","Headphones"]
for i in products:
    print(i)
print("\n")

#tuple
products1=("laptop","Mobile","Tablet","Headphones")
for it in products1:
    print(it)
print("\n")

#set
products2=set(products)
for it1 in products2:
    print(it1)
print("\n")

# Dictonary
products3={"laptop":1000,"Mobile":500,"Tablet":300,"Headphones":100}
for key in products3:
    print("Product name",key)
    print("Product price",products3[key],"\n")
# product3[key] is used to access the value of the key in the dictonary

# range function is used to generate a sequence of numbers
# range(start, stop+1, step)
for i in range(1,11):
    print(i)

for i in range(10,0,-2):
    print(i)