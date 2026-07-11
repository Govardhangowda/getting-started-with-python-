filename=input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        names = file.readlines()
        search_name = input("Enter the name to search: ")
        found = False
        for name in names:
            if search_name.lower() in name.lower():
                print(f"Found: {name.strip()}")
                found = True
        if not found:
            print("Name not found.")
except FileNotFoundError:
    print("File not found.")