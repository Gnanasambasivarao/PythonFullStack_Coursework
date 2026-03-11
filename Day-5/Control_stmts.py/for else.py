# Write a Python program to demonstrate the use of for-else loop.
# The for-else loop is used to execute a block of code when the loop is completed without any break statement.
for i in range(1,11):
    if i == 15:
        break
    else:
        print(i)
else:
    print("Loop is completed")