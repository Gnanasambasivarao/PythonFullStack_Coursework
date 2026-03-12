# String is collection of group of character 
# String is immutable in nature

s="Python"

"""  
String Operation commonly used

1-> Concatination Using + symbol
2-> Repetition Using * symbol
3-> Indexing for accessing the character in the string 
4-> Slicing Using [start:stop:step]
5-> Membership Using in and not in
6-> String Methods
    -> Length of the string using len() function
    -> max() and min() function to find the maximum and minimum character in the string
    -> chr() function to convert ASCII value to character
    -> ord() function to convert character to ASCII value
    -> sorted() function to sort the values
    -> replace() function to replace the string
    -> split() function to split the string into list
    -> count() function to count the number of occurrences of a character in the string
    -> find() function to find the index of the first occurrence of a character in the string
    -> Align methods to align the string using ljust(), rjust(), and center() methods
    -> Strip methods to remove the unwanted characters(Like spaces) from the string using lstrip(), rstrip(), and strip() methods
"""

# Concatination Using + symbol
s1="Hello"
s2="World"
print(s1+s2)

# Repetition Using * symbol
s3="Python"
print(s3*5)

# Indexing for accessing the character in the string
# Indexing starts from 0 to n-1 for forward indexing and -1 to -n for backward indexing
s4="Python"
print(s4[0]) # P
print(s4[1]) # y
print(s4[-1]) # n
print(s4[-2]) # o

# Slicing Using [start:stop:step]
# To extract the group of characters from the string we can use slicing
# In python spaces have index as well 
s5="Python Programming"
print(s5[0:6]) # Python
print(s5[7:18]) # Programming
print(s5[0:18:2]) # Pto rgamn
print(s5[-1:-18:-1]) # gnimmargorP nohtyP
print(s5[::-1]) # gnimmargorP nohtyP

# Membership Using in and not in
s6="Python Programming"
print("Python" in s6) # True
print("Samba" in s6) # False
print("Python" not in s6) # False
print("Samba" not in s6) # True

