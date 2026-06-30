def average(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    return (sum/len(numbers))


print(f'The average is: {average(3,4,5,6)}')
