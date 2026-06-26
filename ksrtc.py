import sys
gender=input('what is your gender: ').lower()
if gender=='female':
    print('0 rupees')
    sys.exit()
age=int(input('what is your age: '))
fare=int(input('what is the fare: '))
if (gender=='female' or age<5):
    print('0 rupees')
elif (13>age>5 or age>60):
    print(f'{fare*(0.5)} rupees')
else:
    print(f' {fare} rupees')
