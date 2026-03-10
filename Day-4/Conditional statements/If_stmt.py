"""
Python is a indentation based language.

Syntax of Simple if statement:

if condition:
    statement1
    statement2
    statement3
"""
if 10>5:
    print("10 is greater than 5")

"""
Syntax of if-else statement:

if condition:
    statement1
else:
    statement2

"""
if(10>5):
    print("10 is greater than 5")
else:
    print("10 is not greater than 5")



"""
Syntax of if-elif-else statement:
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4
"""

a=10
if a>0:
    print("a is positive")
elif a<0:
    print("a is negative")
else:
    print("a is zero")


"""
Syntax for Nested if statement:
if condition1:
    statement1
    if condition2:
        statement2
    elif condition3:
        statement3
    else:
        statement3
else:
    statement4

"""
a=10
if a>0:
    print("a is positive")
    if a%2==0:
        print("a is even")
    else:
        print("a is odd")
else:
    print("a is negative")