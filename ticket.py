i=8
while i>=0:
    bk=input('Ticket booked?: ')
    if bk=='yes':
        i-=1
        print(f'Ticket confirmed, no. of remaining seats: {i}')
    else:
        print(f'Ticket not confirmed, no of available seats: {i}')
        continue
print('All seats are booked')    
