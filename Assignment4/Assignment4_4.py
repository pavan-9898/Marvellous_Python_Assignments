from functools import reduce

def main():

    print("Ënter how many elements: ")
    no=int(input())
    Element=list()
    for i in range(no):
        nums=int(input(f"Eneter the {i+1} element"))
        Element.append(nums)
    print("User Given List is :",Element)

    even_nums=list(filter(lambda x:x%2==0,Element))
    print("Even Numbers :",even_nums)

    square=list(map(lambda x:x*x,even_nums))
    print("List After Map :",square)

    add=reduce(lambda x,y:x+y,square)
    print("List After reduce :",add)


if __name__=="__main__":
    main()