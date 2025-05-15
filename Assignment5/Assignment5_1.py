def sum(no1,no2):
    no3=no1+no2
    return no3

def Difference(no1,no2):
    no3=no1-no2
    return no3

def product(no1,no2):
    no3=no1*no2
    return no3

def Division(no1,no2):
    no3=no1/no2
    return no3

def main():
    print("Enter 1st Number :")
    no1=int(input())
    print("Enter 2nd Number: ")
    no2=int(input())
    result=sum(no1,no2)
    print("sum is :",result)
    diff=Difference(no1,no2)
    print("Difference is :",diff)
    prod=product(no1,no2)
    print("Product is :",prod)
    div=Division(no1,no2)
    print("Division is :",div)

if __name__ == "__main__":
    main()