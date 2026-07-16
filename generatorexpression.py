gen_exp=(x*x for x in range(10))
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1
print(next(gen_exp))  # Output: 4
print(next(gen_exp))  # Output: 9
print(next(gen_exp))  # Output: 16
print(list(gen_exp))  # Output: [25, 36, 49, 64, 81]