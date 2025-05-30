def main():

    print("Enter marks")
    marks=int(input())
    if marks>=90:
        print("Garde A")
    elif marks >=70 and marks<=90:
        print("garde B")
    else:
        print("Grade C")

    print("--------------------")

    nums=[1,2,3,4,5]

    for i in nums:
        if i==3:
            break
        print(i)

    print("---------------")

    for i in nums:
        if i==3:
            continue
        print(i)

if __name__ == "__main__":
    main()