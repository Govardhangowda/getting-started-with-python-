while True:
    try:
        j = int(input("Enter the number of students: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

with open("marks.txt", "w") as file:
    for i in range(j):
        name = input(f"Enter the name of student {i+1}: ")
        marks = input(f"Enter the marks of {name}: ")
        file.write(f"{name}- {marks}\n")
