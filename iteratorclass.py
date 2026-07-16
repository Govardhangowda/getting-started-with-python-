class EvenNumbers:
    def __init__(self, n):
        self.max = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        else:
            result = self.current
            self.current += 2
            return result
        
set1=EvenNumbers(10)
for num in set1:
    print(num)