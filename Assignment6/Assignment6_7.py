def largest(no):
    elements=list()
    for i in range(no):
        nums=int(input(f"Enter {i+1} element :"))
        elements.append(nums)
    print(f"Largest Element is :{max(elements)}")

def main():
    print("Enter Number: ")
    no=int(input())
    # elements=list()
    # for i in range(no):
    #     nums=int(input("Enetr {i+1} element :"))
    #     elements.append(nums)
    # print(f"Largest Element is :{max(elements)}")
    largest(no)

if __name__ == "__main__":
    main()