name=input('What is your name: ')
age=int(input('What is your age: '))
membership='regular'
if age<=18:
    membership='student'
elif age>60:
    membership='senior citizen'

print(f'welcome {name}, You are accepted as {membership} member')
    
