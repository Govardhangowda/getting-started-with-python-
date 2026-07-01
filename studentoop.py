class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display_info(self):
        print(f'Name: {self.name}, Marks : {self.marks}')
    
stdnt1= student('David','24')
stdnt2= student('Salt','34')
stdnt1.display_info()
stdnt2.display_info()
