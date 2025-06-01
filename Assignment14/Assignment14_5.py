class BankAccount:

    def __init__(self,account_number,name,balance):
        self.acccount_number=account_number
        self.name=name
        self.balance=balance
    
    def Deposit(self,balance):

        self.balance=self.balance+balance

    def Withdraw(self,amount):


        self.balance=self.balance-amount
    
    def Display(self):
        print("Account Number :",self.acccount_number)
        print("Account Holder Name :",self.name)
        print("Total Balance Is:",self.balance)

        

def main():

    obj=BankAccount("123456789","pavan",20000)
    obj.Deposit(10000)
    obj.Display() # 30000
    obj.Withdraw(5000)
    obj.Display() # 25000


if __name__ == "__main__":
    main()