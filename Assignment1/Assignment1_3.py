def Add(no1,no2):
    no3=no1+no2
    return no3

def main():
    print("Enter 1st number")
    number1=int(input())
    print("Enter 2nd number")
    number2=int(input())

    result=Add(number1,number2)
    print("Addition is :",result)

if __name__ =="__main__":
    main()