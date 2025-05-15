def area_perimiter(length,width):
    area=length*width
    print("Area of rectangle :",area)

    perimiter= 2*(length + width)
    print("Perimiter of rectangle is :",perimiter)

def main():
    print("Enter the length of rectangle :")
    l=int(input())
    print("Enter the width of rectangle :")
    w=int(input())
    area_perimiter(l,w)


if __name__ == "__main__":
    main()