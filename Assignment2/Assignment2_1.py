import Arithmatic as A
def main():

    print("Enter 1st Number :")
    no1=int(input())
    print("Enter 2nd Number :")
    no2=int(input())
   
    A.Add(no1,no2)
    A.Sub(no1,no2)
    A.Mult(no1,no2)
    A.Div(no1,no2)


if __name__ == "__main__":
    main()