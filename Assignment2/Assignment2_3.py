def fact(n):
   if n==0 or n==1:
       return 1
   else:
       return (n * fact(n-1))

def main():
    print("Enter Number :")
    no=int(input())
    result=fact(no)
    print(f"factorial of {no} is {result} ")
if __name__ == "__main__":
    main()