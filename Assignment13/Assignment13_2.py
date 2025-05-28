class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Deposite(self,Amount):
        
        self.Amount=self.Amount+Amount
        print("Total Amount is :",self.Amount)
    
    def Withdraw(self,Amount1):
       
       print("Requested Withdraw balnce is :",Amount1)
       
       self.Amount= self.Amount-Amount1

    def CalculateInterest(self):
        self.Amount=self.Amount+BankAccount.ROI

    def Display(self):
        print("Name is :",self.Name)
        
        print("Total Balance after withdrawal is :",self.Amount)


def main():

    Obj1=BankAccount("pavan",20000)
    Obj1.Deposite(10000)
    Obj1.CalculateInterest()
    Obj1.Withdraw(5000)
    Obj1.Display()

    print()

    Obj2=BankAccount("Aishwarya",30000)
    Obj2.Deposite(10000)
    Obj2.CalculateInterest()
    Obj2.Withdraw(5000)
    Obj2.Display()


if __name__ == "__main__":
    main()