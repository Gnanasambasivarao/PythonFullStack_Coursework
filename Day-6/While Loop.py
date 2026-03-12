# write a program to print the number upto 20 using while loop

i=20
while i<=30:
    print(i)
    i+=1
print("\n")

# write a program to print the number from 20 to 30 using while loop
# Using break statement to exit the loop when the condition is met
i=20
while i<=30:
    if i==25:
        break
    print(i)
    i+=1
print("\n")

# Using continue statement to skip the current iteration when the condition is met
i=20
while i<=30:
    if i==25:
        i+=1
        continue
    print(i)
    i+=1
    
    
# what is the difference between break, continue, and pass statements?
# break statement is used to exit the loop when the condition is met
# continue statement is used to skip the current iteration when the condition is met
# pass statement is used to do nothing when the condition is met

i=20
while i<=30:
    if i==25:
        pass
    print(i)
    i+=1
    

