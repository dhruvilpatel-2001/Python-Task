# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.
from traceback import print_tb

firstName = input("Enter a first name: ");
lastName = input("Enter a last name: ");

full_name = firstName + " " + lastName

print(f"\nHello {full_name}! Welcome to the python program.");