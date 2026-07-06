class bank:
    def __init__(self,acnt,balance):
        self.acnt=acnt
        self.balance=balance
        
    def check_balance(self):
        return self.balance
        
    def deposit(self):
        add=int(input('Enter deposit amount: '))
        self.balance=self.balance+add
        print(f'Balance after depositing  is: {self.balance}')
        
    def withdraw(self):
        draw=int(input('Enter withdrawl amount: '))
        self.balance=self.balance-draw
        print(f'Balnce after withdrawl is: {self.balance}')
while True:
    print('Welcome to shivamogga bank')
    print('Enter: \n 1.Check Balance \n 2.Deposit Money \n 3.Withdrawl Money \n 4.Exit \n')
    i=(input())
    bnk1=bank('1001',2000)
    if i in {1,2,3,4}:
        if i==1:
            print(f'The balance is {bnk1.check_balance()}')
        elif i==2:
            bnk1.deposit()
        elif i==3:
            bnk1.withdraw()
        else:
            print('Thanks for your time')
            break
    else:
        print('Invalid option')
        
