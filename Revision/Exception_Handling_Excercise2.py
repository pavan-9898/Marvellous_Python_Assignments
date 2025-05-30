def keyboard():

    try:
        print("Enter Number :")
        n=int(input())
        print("Entered Number is :",n)

    except KeyboardInterrupt as key:
        print("User cancelled the input :",key)

    finally:
        print("Finally block executed")

def main():

    keyboard()

if __name__ == "__main__":
    main() 