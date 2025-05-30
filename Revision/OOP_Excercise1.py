from datetime import date

class Person:

    def __init__(self,Name,DOB,City):
        self.Name=Name
        self.DOB=DOB
        self.City=City

    def Age(self):
        
        today=date.today()
        # print(type(today.year))
        age=today.year-self.DOB.year
       
        print("Person Name Is :",self.Name)
        print("Person City Is :",self.City)
        print("Person Age Is :",age)
    

def main():

    Obj1=Person("pavan",date(1998,6,17),"Pune")
    Obj1.Age()

    print()

    Obj2=Person("Aishwarya",date(2002,2,4),"Mumbai")
    Obj2.Age()


if __name__ == "__main__":
    main()