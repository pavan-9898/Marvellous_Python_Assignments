def main():
    print("Enter a number :")
    num=int(input())
    for i in range(2, int(num**0.5) + 1):
        print(i)


if __name__ == "__main__":
    main()