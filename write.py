with open("friends.txt", "w") as file:
    for i in range(3):
        frnd = input(f"Enter the name of friend {i+1}: ")
        file.write(frnd + "\n")
