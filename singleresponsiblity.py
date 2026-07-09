class book:
    def __init__(self,name,author,year):
        self.name=name
        self.author=author
        self.year=year

class details:
    def printdetail(self,book):
        print(f'The book is: {book.name}')
        print(f'The author is: {book.author}')
        print(f'The year of publication is: {book.year}')

bk1=book('steve jobs','Walter Issacson',2010)
detail=details()
detail.printdetail(bk1)