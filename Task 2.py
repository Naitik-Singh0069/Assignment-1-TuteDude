''' Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

first = input("Enter your first name: ")
last = input("Enter your last name: ")
full_name = first + " " + last
print("Hello, " + full_name + "! Welcome to Python Programming")