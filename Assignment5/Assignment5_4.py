def largest(no1,no2,no3):
    if no1>=no2 and no1>=no3:
        print(f"largest Number Is :",no1)            
    elif no2>=no1 and no2>=no3:
         print(f"Largest Number Is :",no2)
    else:
        print(f"Largext Number IS :",no3)
    
def main():
    print("Enter 1st number ")
    x=int(input())
    print("Enter 2nd number ")
    y=int(input())
    print("Enter 3rd number ")
    z=int(input())
    largest(x,y,z)

if __name__ == "__main__":
    main()