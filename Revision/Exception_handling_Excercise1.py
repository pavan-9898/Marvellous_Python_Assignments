def Division(no1,no2):

    try:
        Ans=no1/no2
        print("Division is :",Ans)

    except ZeroDivisionError as z:
        print("Exception occured due to second input :",z)
    
    finally:

        print("Finally block executed")

def main():

    Division(10,0)

if __name__ == "__main__":
    main()