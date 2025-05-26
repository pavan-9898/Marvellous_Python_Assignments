class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.value2=0
    
    def Accept(self):
        print("Enter First Value :")
        self.Value1=int(input())
        print("Enter Second Value :")
        self.Value2=int(input())

       
    def Addition(self):
        result=self.Value1+self.Value2
        print("Addition is :",result)

    def Substraction(self):
        result=self.Value1-self.Value2
        print("Substraction is :",result)

    def Multiplication(self):
        result=self.Value1*self.Value2
        print("Multiplication is :",result)

    def Division(self):
        result=self.Value1/self.Value2
        print("Division is :",result)


def main():
    Obj1=Arithmetic()
    Obj1.Accept()
    Obj1.Addition()
    Obj1.Substraction()
    Obj1.Multiplication()
    Obj1.Division()

    print("-----------------")

    Obj2=Arithmetic()
    Obj2.Accept()
    Obj2.Addition()
    Obj2.Substraction()
    Obj2.Multiplication()
    Obj2.Division()

if __name__ =="__main__":
    main() 