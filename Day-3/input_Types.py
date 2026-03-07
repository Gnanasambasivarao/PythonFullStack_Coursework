name="python"
print(name)
print(type(name))

na= input("Enter your name: ")
print(na)
age= input("Enter your age: ")
print(age)
print(type(age))

age1= int(age)
print(age1)
print(type(age1))

price= input("Enter the price: ")
print(price)
print(type(price))

price1= float(price)
print(price1)
print(type(price1))

print("Samba siva rao")
print("Samba siva rao".split(" "))

names=input("Enter your names: ")
print(names)
namess= names.split(" ")
print(namess)

numbers=input("Enter the numbers: ")
print(numbers)

'''numbers1=int(input("Enter the numbers: ").split())
print(numbers1)
int() argument must be a string, a bytes-like object or a number, not 'list'
'''

number1= list(map(int, input("Enter the numbers: ").split()))
print(number1)

number2= list(map(float, input("Enter the numbers: ").split()))
print(number2)

number3= tuple(map(int, input("Enter the numbers: ").split()))
print(number3)

number4= tuple(map(float, input("Enter the numbers: ").split()))
print(number4)

names1=set(input("Enter the names: ").split())
print(names1)

num2= set(map(int,input("Enter the numbers:").split()))
print(num2)

num3= set(map(float,input("Enter the numbers:").split()))
print(num3)

d=eval(input("Enter the inputs: "))
print(d)

username,password=['py','py123']
print(username)
print(password)

username1,password1= input("Enter the username and password: ").split()
print(username1)
print(password1)

username2,password2= map(input("Enter the username and password: ").split())
print(username2)
print(password2)

username3,password3= list(map(input("Enter the username and password: ").split()))
print(username3)
print(password3)
