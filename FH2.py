import os

print("Checking if my_file exists or not...")

if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file = open("my_file.txt", "w")

my_file.write("I'm Ashna Shrestha and I'm 13 yrs old.")

my_file.close()

print("File created successfully!")