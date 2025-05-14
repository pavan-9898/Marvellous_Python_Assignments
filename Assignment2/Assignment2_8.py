def pattern(n):
    num=1
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num,end=" ")
            num+=1
        print(" ")
        
      
def main():

    print("Enter Number :")
    no=int(input())

    pattern(no)

if __name__ =="__main__":
    main()