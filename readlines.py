j=0
js=input("Enter the name of the file to read: ")
with open(js, "r") as file:
    lines = file.readlines()
    for line in lines:
        j += 1
print(f"Number of lines in the file: {j}")