class calculator:

    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    
    
    def Add(self):
        no3=self.no1+self.no2
        print("Addition is :",no3)
    
    def Sub(self):
        no3=self.no1-self.no2
        print("Substraction is:",no3)

    def Mul(self):
        no3=self.no1*self.no2
        print("Multiplication is :",no3)
    
    def Div(self):
        
        try:
            no3=self.no1/self.no2
            print("Division is :",no3)
        except ZeroDivisionError as z:
            print("Exception occured due to second input please enter valid input :",z)


def main():

    print("Enter 1st Number")
    no1=int(input())
    print("Enter 2nd Number")
    no2=int(input())

    obj=calculator(no1,no2)
    obj.Add()
    obj.Sub()
    obj.Mul()
    obj.Div()

if __name__ == "__main__":
    main()