def sum_digit(no):
    sum=0
    for i in str(no):
       sum+=int(i)
    return sum

def main():

    print("Enter Number :")
    no=int(input())
    add=sum_digit(no)
    print("Addition is ",add)

if __name__ == "__main__":
    main()