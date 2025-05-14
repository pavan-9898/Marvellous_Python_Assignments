def ChkNum_pnz(no1):
    if no1<0:
        print("Negative Number")
    elif no1 >0:
        print("positive Number")
    else:
        print("Zero")

def main():
    
    print("Enter Number")
    no=int(input())

    ChkNum_pnz(no)

if __name__=="__main__":
    main()
