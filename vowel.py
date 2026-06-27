j=0
str=input('Input: ').lower()
for i in str:
    if i in 'aeiou':
        print(i)
        j+=1
    else:
        continue
print(f'No  of vowels: {j}')
