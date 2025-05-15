from functools import reduce

def main():
    print("Enter how Many Elements :")
    no=int(input())
    elements=list()
    for i in range(no):
        nums=int(input(f"Eneter the {i+1} element :"))
        elements.append(nums)
    print("User Given List :",elements)

    prime=list(filter(lambda num: num > 1 and all(num % i for i in range(2, int(num**0.5) + 1)),elements))
    print("List After Filter :",prime)

    mul=list(map(lambda x:x*2,prime))
    print("list Aftre Map :",mul)

    maximum =reduce(lambda x,y:max(x,y),mul)
    print("List After Reduce :",maximum)




if __name__ =="__main__":
    main()