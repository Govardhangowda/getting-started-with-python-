class bankaccount:
    def __init__(self,accountnumber,balance):
        self.__accountnumber=accountnumber
        self.__balance=balance
        
    def checkbalance(self):
        print(f'Balance: {self.__balance}')
        
    def withdrawl(self):
        amount=int(input('Withdrawl Amount: '))
        self.__balance=self.__balance-amount
        print(f'Blance after withdrawing is: {self.__balance}')
        
    def deposit(self):
        amount=int(input('Deposit Amount: '))
        self.__balance=self.__balance+amount
        print(f'Balance after depositing is: {self.__balance}')
        
acnt1=bankaccount('1001',2000)
acnt2=bankaccount('1002',3000)
acnt1.deposit()
acnt2.withdrawl()
