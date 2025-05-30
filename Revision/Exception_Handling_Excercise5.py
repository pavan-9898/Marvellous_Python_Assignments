def value_exception():

    try:
        print("Enter Number :")
        n=int(input())
        print("Entered number is :",n)
    except ValueError as v:
        print("You have entered wrong input :",v)
    finally:
        print("Finally block executed")

def main():
    
    value_exception()


if __name__ == "__main__":
    main()