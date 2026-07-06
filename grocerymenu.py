cart={}
while True:
    print('Welcome to Dmart groceries')
    print('Enter:\n  1.add items\n  2.remove items\n  3.view price\n  4.exit ')
    i=int(input())
    if i in [1,2,3,4]:
        if i==1:
            item=input('item name: ')
            price=int(input('item price: '))
            cart[item]=price
        elif i==2:
            ite=input('item name to be deleted: ')
            del cart[ite]
        elif i==3:
            price=sum(cart.values())
            print(f'the groceries are {list(cart.items())}')
            print(f'Total price of your groceries is: {price}')
        else:
            print('Thanks for your time')
            break
    else:
        print(f'Invalid input')
