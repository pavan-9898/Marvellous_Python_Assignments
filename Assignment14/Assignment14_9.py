class Product:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __eq__(self, value):

        if isinstance(value,Product):
            return self.price==value.price
        return False
        
        

def main():

 obj1=Product("xyz",10000)
 obj2=Product("wxu",10000)
 obj3=Product("xyz",5000)

 print(obj1==obj2)  #True
 print(obj2==obj3)  # False



if __name__ =="__main__":
    main()