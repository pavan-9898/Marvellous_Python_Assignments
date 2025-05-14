def Divisible_by_5(no1):
    if no1 %5==0:
        print("True")
    else:
        print("False")
def main():
    print("Enter the number")
    no=int(input())
    Divisible_by_5(no)
 
if __name__ =="__main__":
    main()