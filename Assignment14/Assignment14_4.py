class Student:

    school_name="Modern College"

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        Student.school_name="SP College"  # changed school_name varible value using class name
    
    def Display(self):

        print("Student Name Is :",self.name)
        print("Student Roll_No Is :",self.roll_no)
        print("Student School Name :",Student.school_name)

def main():
     
    obj=Student("pavan",201)
    obj.Display()


if __name__ == "__main__":
    main()
    