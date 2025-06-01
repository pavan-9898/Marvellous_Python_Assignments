class Book:

    def __init__(self,price):
        self.__price=price
        
    def Get(self):

        print("Price Of Book Is :",self.__price)

    
def main():

   obj1=Book(500)
   obj1.Get()
    # print(obj1.__price)
    
if __name__ =="__main__":
    main() 