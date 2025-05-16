def main():
    print("Enter Number :")
    no=int(input())
    square= lambda no :no*no
    print("Square is :",square(no))
    cube=lambda no :no*no*no
    print("Cube is :",cube(no))

if __name__ == "__main__":
    main()