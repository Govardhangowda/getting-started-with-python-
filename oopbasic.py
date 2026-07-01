class Mobile:
    def __init__(self,brand,price):
        self .brand = brand
        self .price = price
        
    def display__info(self):
        print(f'Phone brand: {self.brand},price : {self.price}')
        
S24= Mobile('Samsung','69999')
iphone17=Mobile('Apple','169999')
S24.display__info()
iphone17.display__info()
