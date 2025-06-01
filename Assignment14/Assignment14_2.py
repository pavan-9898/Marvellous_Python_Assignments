class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def Area(self):
        A=self.width*self.length
        print("Area Of Rectangle Is: ",A)
    
    def Perimiter(self):
        p=2*self.width+self.length
        print("Perimiter Of Rectangle :",p)

def main():

    obj1=Rectangle(50,30)
    obj1.Area()
    obj1.Perimiter()

if __name__ == "__main__":
    main()