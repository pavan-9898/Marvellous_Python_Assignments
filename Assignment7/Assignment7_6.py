def prime_check(numbers):
    prime=list(filter(lambda num: num > 1 and all(num % i for i in range(2, int(num**0.5) + 1)),numbers))
    print("prime Numbers :",prime)

def main():
    print("How many elements ?")
    no=int(input())
    numbers=list()
    for i in range(no):
        num=int(input(f"Enter {i+1} element "))
        numbers.append(num)
    print("Entered List :",numbers)

    prime_check(numbers)

    # prime=list(filter(lambda num: num > 1 and all(num % i for i in range(2, int(num**0.5) + 1)),numbers))
    # print("prime Numbers :",prime)


if __name__ == "__main__":
    main()