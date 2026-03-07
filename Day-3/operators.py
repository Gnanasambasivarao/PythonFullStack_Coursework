# Arithematic operators
a=10
b=5

print(a+b) #Addition 
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a//b) #Floor division returns the quotient in integer form
print(a%b) #Modulus returns the remainder
print(a**b) #Exponentiation 

# comparison operators
print(a==b) #Equal to
print(a!=b) #Not equal to
print(a>b) #Greater than
print(a<b) #Less than
print(a>=b) #Greater than or equal to
print(a<=b) #Less than or equal to

# logical operators
x= True
y= False
print(x and y) #Logical AND returns True if both the operands are true
print(x or y) #Logical OR returns True if either of the operands is true
print(not x) #Logical NOT returns the opposite of the operand
print(not y) #Logical NOT returns the opposite of the operand


# Assignment operators
c=10
c+=5 #c=c+5
print(c)
c-=5 #c=c-5
print(c)
c*=5 #c=c*5
print(c)
c/=5 #c=c/5
print(c)
c//=5 #c=c//5
print(c)
c%=5 #c=c%5
print(c)

# Bitwise operators
a=10 #In binary 1010
b=5 #In binary 0101
print(a & b) #Bitwise AND returns 1 if both the bits are 1
print(a | b) #Bitwise OR returns 1 if either of the bits is
print(a ^ b) #Bitwise XOR returns 1 if the bits are different
print(~a) #Bitwise NOT returns the complement of the bits
print(a << 1) #Bitwise left shift shifts the bits to the left by the
print(a >> 1) #Bitwise right shift shifts the bits to the right by the specified number of positions

# Membership operators
list1=[1,2,3,4,5]
print(3 in list1) #Returns True if the value is found in the list
print(6 in list1) #Returns False if the value is not found in the list
print(3 not in list1) #Returns False if the value is found in the list
print(6 not in list1) #Returns True if the value is not found in the list
"""
In dictionary it checks for the keys not the values
"""
dict={"name":"Samba siva rao","age":30}
print("name" in dict) #Returns True if the key is found in the dictionary

print("Samba siva rao" in dict) #Returns False if the value is not found in the dictionary

# Identity operators
""" 
Identity operators are used to compare the memory locations of two objects.
The "is" operator returns True if both the operands refer to the same object in memory, 
while the "is not" operator returns True if both the operands do not refer to the same object in memory.
"""
a=10
b=10
print(a is b) #Returns True if both the operands refer to the same object
print(a is not b) #Returns False if both the operands refer to the same object

