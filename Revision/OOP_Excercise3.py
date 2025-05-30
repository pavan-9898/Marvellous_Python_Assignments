class Demo: # class 
    x=10 # class Varibale

    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2

    
def main():
    obj1=Demo(10,11)
    print("value of i is :",obj1.i)
    print("value of j is :",obj1.j)

    print()

    obj2=Demo(50,60)
    print("Value of i is :",obj2.i)
    print("Value of j is :",obj2.j)


    print("class varibale is :",Demo.x) # printing Calss Varibale


if __name__ == "__main__":
    main()