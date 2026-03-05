#Example concepts using rules of variable creation in python.
#Rule1
Myname="Samba"
_age=21
dob_1= "12/08/2004"

print(Myname)
print(_age)
print(dob_1)

#Rule2: If we use number at first then it through SyntaxError

"""
2_name="Samba"
2age=21
print(2_name)
print(2age)

Output will be like this 
        Cell In[4], line 26
            2_name="Samba"
            ^
        SyntaxError: invalid decimal literal
"""
#Rule3 : Case sensitive

Myname="Samba"
myName="siva"
print(Myname)
print(myName)

#Rule4: Uasge of keyword as variabe name
"""
 for ="job ready"
 while="Studing Data Science"
 print(for)
 print(while)

If we use then it throw and Syntax Error like this:
    for ="job ready"
        ^
SyntaxError: invalid syntax

"""