from functools import reduce
marks = [35, 50, 66, 20, 88, 75]
update=list(map(lambda x: x + 5, marks))
filtered=list(filter(lambda x: x >= 50, update))
total=reduce(lambda x, y: x + y, filtered)
print(f'after marks update: {update}')
print(f'filtered marks: {filtered}')
print(f'total: {total}')