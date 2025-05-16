def even(numbers):
    even_numbers=list(filter(lambda x :x%2==0,numbers))
    print("Even Numbers :",even_numbers)

def main():
    print("How many Elements ? :")
    no=int(input())
    numbers=list()
    for i in range(no):
        num=int(input(f"Enter {i+1} element"))
        numbers.append(num)
    print("Entered List is :",numbers)

    even(numbers)

    # even_numbers=list(filter(lambda x :x%2==0,numbers))
    # print("Even Numbers :",even_numbers)

if __name__ == "__main__":
    main()