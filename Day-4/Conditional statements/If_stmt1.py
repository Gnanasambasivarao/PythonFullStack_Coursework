# Simple If Statement example 
min_balance = 5000
cur_balance = 4500
if cur_balance < min_balance:
    print("Your account balance is low. Please deposit more money.")

# Example for if-else statement
data = ("Samba@gmail.com", "Siva123")
mail= input("Enter your email: ")
password= input("Enter your password: ")
# mail == data[0] and password == data[1]
if data == (mail, password):
    print("Login successful")
else:
    print("Invalid email or password")


# Example2 for if-else statement
fruits = ["apple", "banana", "orange"]
required_fruit = input("Enter the fruit you want to buy: ")
if required_fruit in fruits:
    print(f"{required_fruit} is available in the store. You can buy it.")
else:
    print(f"{required_fruit} is not available in the store. Please choose another fruit.")

# Example for if-elif-else statement
attendance = int(input("Enter your attendance percentage: "))
if attendance >= 75:
    print("You are eligible to sit for the exam.")
elif attendance >= 50:
    print("You are not eligible to sit for the exam, but you can attend the classes.")
else:
    print("Go and Meet Hod for Permission.")

# Example2 for if-elif-else statement
time = int(input("Enter the time in 24-hour format (0-24): "))
if( 0<=time<=6):
    print("NEO\n intercity\n apstrc\n ts superluxry \n")
elif(7<=time<=12):
    print("express\n apstrc Indra \n ts nonExpress \n")
elif(13<=time<=18):
    print("apstrc superluxry\n ts superluxry \n")
elif(19<=time<=24):
    print("apstrc superluxry\n Intercity \n Morning Star")
else:
    print("Invalid time. Please enter a value between 0 and 24.")

# Example for Nested if statement
login=True
premium_user=True
if login:
    print("Welcome to Jio Hotstar")
    if premium_user:
        print("You have access to premium features. video will play with high quality ")
    else:
        print("Playing the video with noraml quality and Ads ")
else:
    print("Please login to access the content on Jio Hotstar ")


# Example2 for Nested if statement
print("Welcome to the online movie ticket booking system!\n Please select a seat type from the following list:\n sleeper\n General\n AC\n AC economy") 
user= input("Enter your Seat Required: ")
if user =="sleeper":
    print("You have selected Sleeper class. Please select a seat number from 1 to 50.")
    seat_number = int(input("Enter your seat number: "))
    if 1 <= seat_number <= 50:
        print(f"You have successfully booked a Sleeper class seat number {seat_number}.")
    else:
        print("Invalid seat number. Please select a seat number between 1 and 50.")
elif user == "general":
    print("You have selected General class. Please select a seat number from 51 to 100.")
    seat_number = int(input("Enter your seat number: "))
    if 51 <= seat_number <= 100:
        print(f"You have successfully booked a General class seat number {seat_number}.")
    else:
        print("Invalid seat number. Please select a seat number between 51 and 100.")
elif user == "AC":
    print("You have selected AC class. Please select a seat number from 101 to 150.")
    seat_number = int(input("Enter your seat number: "))
    if 101 <= seat_number <= 150:
        print(f"You have successfully booked an AC class seat number {seat_number}.")
    else:
        print("Invalid seat number. Please select a seat number between 101 and 150.")
elif user == "AC economy":
    print("You have selected AC economy class. Please select a seat number from 151 to 200.")
    seat_number = int(input("Enter your seat number: "))
    if 151 <= seat_number <= 200:
        print(f"You have successfully booked an AC economy class seat number {seat_number}.")
    else:
        print("Invalid seat number. Please select a seat number between 151 and 200.")
else:
    print("Invalid seat type. Please select a valid seat type from the list.")

