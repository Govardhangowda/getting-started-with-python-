while True:
    try:
        a=int(input("Enter number: "))
        b=int(input("Enter another number: "))
        result=a/b
        print("Result:", result)
        break  # Exit the loop if input is valid
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")