class Employee:

    def __init__(self,salary,department,name):
        self.__salary=salary  #private 
        self._dept=department # protected 
        self.name=name  #public

def main():
    
    obj=Employee(150000,"IT","Pavan")
    
   
    print("Employee Name :",obj.name)  #public Allowed
    print("Employee Department :",obj._dept) # Private is Allowed
    #print("Employee Salary :",obj.__salary) # Private Not  Allowed it will generate error


if __name__ == "__main__":
    main()