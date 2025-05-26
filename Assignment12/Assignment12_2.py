class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        print("Enter Radius")
        self.Radius=int(input())
        return self.Radius

    def CalculateArea(self,R):
        
        self.Area=Circle.PI*R*R
        # print("Are of circle is :",self.Area)

    def CalculateCircuference(self,R):
        
        self.Circumference=2*Circle.PI*R
        # print("Circumference of circle is :",self.Circumference)

    def Display(self):
        print("Radius of Circle is :",self.Radius)
        print("Area of Circle is :",self.Area)
        print("Circumference of Circle is :",self.Circumference)

def main():
    Obj1=Circle()
    Radius=Obj1.Accept()
    Obj1.CalculateArea(Radius)
    Obj1.CalculateCircuference(Radius)
    Obj1.Display()

    print("-------------")

    Obj2=Circle()
    Radius=Obj2.Accept()
    Obj2.CalculateArea(Radius)
    Obj2.CalculateCircuference(Radius)
    Obj2.Display()

if __name__ == "__main__":
    main()