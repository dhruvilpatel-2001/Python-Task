# Task 1: Read a File and Handle Errors

try:
    with open("Assignment-4/sample.txt", "r") as file:
        print("File Content:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
