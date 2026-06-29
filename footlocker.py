purchase={'puma ferarri':'4000','adidas':'3000','nike':'6000','asics':'3900'}
total=0
for item,price in purchase.items():
    total=total+int(price)
    print(f'the price of {item} is {price}')
    
print(f'total price is:{total}')
