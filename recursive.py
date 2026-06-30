def addon(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    x=n+addon(n-1)
    return x
print(f'the addition of previous no is: {addon(int(input('Enter the number:')))}')
