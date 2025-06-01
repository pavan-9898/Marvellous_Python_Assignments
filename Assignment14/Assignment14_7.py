class Person: # Base Class 

    def __init__(self,name,age):
        print("Person Name Is:",name)
        print("Person Age Is :",age)
    

class Teacher(Person): #Derived Class

    def __init__(self,subject,salary):
      
     super().__init__("pavan",28)  # calling base class

        
     print("Subject Is :",subject)
     print("Salary Is: ",salary)
        
        
def main():

    
    obj2=Teacher("Maths",25000)
    


if __name__ =="__main__":
    main()