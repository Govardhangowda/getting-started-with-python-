class employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary
        
    def display(self):
        print(f'{self.name} is the {self.designation}. and salary is {self.salary}')
        
emply1=employee('David','asst. manager')
emply2=employee('Salt','Manager',40000)
emply1.display()
emply2.display()
