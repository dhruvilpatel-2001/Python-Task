# Task 2: Using the Math Module for Calculations

import math

# Ask a input from user
num = float(input("Enter a number: "))

sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# Display a provided results
print(f"Square root of {num} is: {sqrt_val}")
print(f"Natural log of {num} is: {log_val}")
print(f"Sine of {num} radians is: {sine_val}")
