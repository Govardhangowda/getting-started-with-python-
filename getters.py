class bankaccount:
    def __init__(self,accountno,balance):
        self.accountno=accountno
        self.balance=balance
        
    def get_balance(self):
        return self.balance
        
    def updatebalance(self):
        update=int(input('amount: '))
        if ((-1)*update)>(self.balance):
            print('Not sufficient amount in balance')
        else:
            self.balance=self.balance+update
            print(f'The balnce now is: {self.balance}')
            
