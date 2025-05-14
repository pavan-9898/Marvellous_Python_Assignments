def check_prime(no):
    if no%2!=0:
        print("Number is Prime")
    else:
        print("Number Is Not Prime")

def main():
    print("Enter Number :")
    no=int(input())
    check_prime(no)
if  __name__ == "__main__":
    main()