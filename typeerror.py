while True:
    try:
        age=int(input("Enter your age: "))
        print("Your age is:", age)
        print(f"You need {100-age} years to reach 100.")
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid integer for age.")