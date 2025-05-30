def Positional_Addition(no1,no2):
    return no1+no2

def Keyword_Addition(no1,no2):
    return no1+no2

def Default_Addition(no1,no2=70):
    return no1+no2

def Variable_Addition(*no):
    sum=0
    for i in no:
        sum=sum+i
    return sum


## Inner Function Example:

def fun1(msg):
    def fun2():
        print(msg)
    fun2()


    ## Recursion

def Recursion(num):
    if num==0:
        return 1
    else:

     return num * Recursion(num-1)
       
         
def main():

    ret=Positional_Addition(10,20)
    print("using positional  argument addition is :",ret)

    ret=Keyword_Addition(no2=50,no1=20)
    print("using  keyword argument addition is :",ret)

    ret=Default_Addition(20)
    print("using  default argument addition is :",ret)

    ret=Variable_Addition(10,20,30)
    print("using  variable argument addition is :",ret)

    print("------------")

    fun1("Hello this is inner function example ")

    print("----------------")

    ret=Recursion(5)
    print("factorial using recursion is :",ret)



if __name__ == "__main__":
    main()