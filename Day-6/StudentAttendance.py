# WAP to understand the attendance system for students using for loop
data={}
n= int(input("Enter the number of students:"))
for i in range(n):
    names=input("Enter the name of the student: ")
    data[names]=False
    print("\n")
    
for name in data:
    user_input=int(input(f"Is { name } is Present? (1/0)"))
    if user_input==1:
        data[name]=bool(user_input)
    else:
        data[name]=bool(user_input)
else:
    print("Attendance is taken sucessfully")
    print(data)
    

# WAP to understand the attendance system for students using while loop and For loop
n= int(input("Enter the number of students:"))
while n>0:
    names=input("Enter the name of the student: ")
    data[names]=False
    n-=1
    print("\n")
else:
    print("Data Added Successfully")
    print(data)
    
for name in data:
    user_input=int(input(f"Is { name } is Present? (1/0)"))
    if user_input==1:
        data[name]=bool(user_input)
    else:
        data[name]=bool(user_input)