from functools import reduce

def prod_fltr(numbers):
     fltr=reduce(lambda x,y:x*y,numbers)
     print("product :",fltr)

def main():
    print("How many elements ? :")
    no=int(input())
    numbers=list()
    for i in range(no):
        num=int(input(f"Enter {i+1} element "))
        numbers.append(num)
    print("Entered List : ",numbers)

    prod_fltr(numbers)

    # fltr=reduce(lambda x,y:x*y,numbers)
    # print("product :",fltr)

if __name__ == "__main__":
    main()

  