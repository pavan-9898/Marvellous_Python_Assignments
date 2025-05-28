class BookStore:  # class Name
    NoOfBooks=0   # class Variable

    def __init__(self,Name,Author):  # Constructor
        self.Name=Name  # instance Variable
        self.Author=Author # instance Variable

        BookStore.NoOfBooks+=1  # incrementing  the Book value by 1
    
    def Display(self):  # instance method
        print("Book Name is :",self.Name)
        print("Book Author is: ",self.Author)
        print("Number of books :",BookStore.NoOfBooks)
    

def main():

    Obj1=BookStore("Linux System Programming","Robert Love") # creating Object as Obj1
    Obj1.Display() # calling Display method 

    print()

    Obj2=BookStore("C Programming","Dennis Ritche") # creating Object as Obj2
    Obj2.Display() # calling display method 


if __name__ == "__main__":
    main()