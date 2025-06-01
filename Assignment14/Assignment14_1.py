class Employee:

    def __init__(self,name,emp_id,salary):
        self.name=name
        self.id=emp_id
        self.salary=salary

    def Display(self):

        print("Employee Name Is: ",self.name)
        print("Employee ID Is :",self.id)
        print("Employee Salary Is :",self.salary)

def main():

    obj1=Employee("Rohit",101,50000)
    obj1.Display()

    print()

    obj2=Employee("pavan",102,150000)
    obj2.Display()



if __name__ == "__main__":
    main()