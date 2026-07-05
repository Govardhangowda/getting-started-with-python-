from abc import ABC, abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    
class manager(employee):
    def __init__(self,rateperhour,workinghours):
        self.rateperhour=rateperhour
        self.workinghours=workinghours
        
    def calculate_salary(self):
        print(f'The salary of manager is: {(self.rateperhour)*(self.workinghours)}')
        
ramesh=manager(300,8)
ramesh.calculate_salary()
