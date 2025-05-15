from functools import reduce
# def reds(Element):
#      product=reduce(lambda x,y:x*y,Element)
#      print("Product Of All Elements Is :",product)

# def fltr(Element):
#     fltr=list(filter(lambda x:x>=70 and x<=90,Element))
#     print("Flitered List Is :",fltr)

# def mp(fltr):
#     mp=list(map(lambda x:x+10,fltr))
#     print("After Adding 10 in Each Element :",mp)

def main():
    print("Enter How many elements :")
    num=int(input())
    Element=list()
    for i in range(num):
        numbers=int(input(f"Enter the  {i+1} elements:"))
        Element.append(numbers)

    # fltr(Element)  
    # reds(Element)
    # mp(Element)
    fltr=list(filter(lambda x:x>=70 and x<=90,Element))
    print("List after filter :",fltr)

    mp=list(map(lambda x:x+10,fltr))
    print("List after map :",mp)

    product=reduce(lambda x,y:x*y,mp)
    print("product Of all elements is :",product)

if __name__ == "__main__":
    main()