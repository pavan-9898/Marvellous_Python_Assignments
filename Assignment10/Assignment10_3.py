from functools import reduce
def fltr():
    print("How many elements :")
    numbers=int((input()))
    my_list=list()
    for i in range(numbers):
        nums=int(input(f"Enter {i+1} element :" ))
        my_list.append(nums)
    print("Input List : ",my_list)

    my_filter=list(filter(lambda x:x>=70 and x<=90,my_list))
    print("List After Filter : ",my_filter)

    my_map=list(map(lambda x:x+10,my_filter))
    print("List After Map :",my_map)

    my_reduce=reduce(lambda x,y:x*y,my_map)
    print("List Afetr Reduce :",my_reduce)

     
def main():

      fltr()
    # print("How many elements :")
    # numbers=int((input()))
    # my_list=list()
    # for i in range(numbers):
    #     nums=int(input(f"Enter {i+1} element :" ))
    #     my_list.append(nums)
    # print(my_list)

if __name__ == "__main__":
 main()
 