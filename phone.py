class phone:
    def __init__(self,name,number=101):
        self.name=name
        self.number=number
        
    def call_contact(self):
        connect=input('Number; ')
        print(f'{self.number} calling to {connect}')
        
    def take_picture(self):
        print(f'Picture taken')
        
phn1=phone('David',1001)
phn1.call_contact()
phn1.take_picture()
        
