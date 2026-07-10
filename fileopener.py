while True:
    try:
        file_path = input("Enter the file to open: ")
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
            break
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please try again.")