class shape:
    def calculate_area(self):
        print('The area of the shape is: ')
        
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calculate_area(self):
        print(f'The area of the figure is:  {((self.length)*(self.breadth))}')
        
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        
    def calculate_area(self):
        print(f'The area of the figure is: {((self.radius)**2)*(3.14)}')
        
rect=rectangle(12,13)
circ=circle(4)
rect.calculate_area()
circ.calculate_area()
