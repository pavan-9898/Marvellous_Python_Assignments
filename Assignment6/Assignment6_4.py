def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=i*fact
        no=no-1
    print(f"factorial  is {fact}")

def main():
    print("Enter a Number")
    num=int(input())
    # fact=1
    # for i in range(1,num+1):
    #     fact=i*fact
    #     num=num-1
    # print(f"factorial  is {fact}")
    factorial(num)


if __name__ == "__main__":
    main()