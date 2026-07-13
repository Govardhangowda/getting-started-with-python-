
import random
lis=[]
for i in range(5):
    lis.append(input("Enter name for entry {}: ".format(i+1)))
print("Lottery entries:", lis)
print("Total entries:", len(lis))
print("Randomly selected winner:", random.choice(lis))