from functools import reduce

def FMR():
    num=[1,2,3,4,5,6]
    print("Original List Is: ",num)

    even=list(filter(lambda x:x%2==0,num))
    print("Even Numbers Are :",even)

    Add=list((map(lambda x:x+10,num)))
    print("List After Adding 10 In Each Item :",Add)

    Sum=reduce(lambda x,y:x+y,num)
    print("Sum of all numbers in list is :",Sum)



def main():
    FMR()

if __name__ == "__main__":
    main()