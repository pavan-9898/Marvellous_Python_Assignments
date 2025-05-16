def main():
    print("Enter How many elements :")
    num=int(input())
    numbers=list()
    for i in range(num):
         no=(int(input(f"Enter the {i+1} element :")))
         numbers.append(no)
    print("Ëntered List : ",numbers)

    double=list(map(lambda x:x*2,numbers))
    print("Doubled List : ",double)

if __name__ == "__main__":
    main()