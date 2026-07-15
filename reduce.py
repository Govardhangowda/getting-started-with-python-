from functools import reduce
scores = [45, 67, 89, 34, 76, 90]
max=reduce(lambda a, b: a if a > b else b, scores)
print(max)