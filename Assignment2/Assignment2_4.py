def fact_sum(no):
    if no<=0:
        print("Number Must Be Positive")
    else:
        total=0
        for i in range(1,no+1):
            if no%i==0:
                total+=i
        return total


def main():

    print("Enter number :")
    no=int(input())
    sum=fact_sum(no)
    print("sum is :",sum)

if __name__ == "__main__":
    main()