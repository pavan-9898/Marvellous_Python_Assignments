class Demo:

    def __init__(self,value1,value2):
        self.i=value1
        self.j=value2
    
    def fun(self):
        print("Inside Fun method ")
        print("value of i and j is ",self.i, "and" ,self.j)
    
    def Add(self):
        print("Addition is ",self.i+self.j)

def main():

    obj1=Demo(10,11)
    obj1.fun()
    obj1.Add()

    print()

    obj2=Demo(50,60)
    obj2.fun()
    obj2.Add()




if __name__ == "__main__":
    main()