def pattern(no):

    
    for i in range(no):
        for i in range(no):
            print(i+1,end=" ")
        print()
        

def main():

    print("Enter Number :")
    no=int(input())

    pattern(no)

if __name__ =="__main__":
    main()