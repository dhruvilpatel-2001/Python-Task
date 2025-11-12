# Task 2: Write and Append Data to a File

# take a input and write to the file
user_input = input("Enter some text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data written successfully!")

# add a additional data
append_input = input("Enter more text to append: ")

with open("output.txt", "a") as file:
    file.write(append_input + "\n")

print("Data appended successfully!")

#Read and display data
print("\nFinal file content:")
with open("output.txt", "r") as file:
    print(file.read())
