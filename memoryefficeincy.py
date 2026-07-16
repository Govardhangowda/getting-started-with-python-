
import sys


genlist=(x for x in range(1000000))
explist=[x for x in range(1000000)]
print(list(genlist))  # Output: [0, 1, 2, ..., 999999]
print(explist)  # Output: [0, 1, 2, ..., 999999]
print(sys.getsizeof(genlist))  # Output: 112
print(sys.getsizeof(explist))  # Output: 8697456