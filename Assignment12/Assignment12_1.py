class Demo:
    value="Demo"
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
    def Fun(self):
        print("Value of No1 is ",self.No1)
        print("Value of No2 is ",self.No2)
    
    def Gun(self):
        print("Value of No1 is ",self.No1)
        print("Value of No2 is ",self.No2)



def main():

    Obj1=Demo(11,21)
    Obj2=Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()


if __name__ == "__main__":
    main()