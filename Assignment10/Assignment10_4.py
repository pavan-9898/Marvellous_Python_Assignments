from functools import reduce

def fltr_map_reduce():
    print("How many elements :")
    no=int(input())
    my_list=list()
    for i in range(no):
        
        nums=int(input(f"Enter {i+1} element:"))
        my_list.append(nums)
    print("Input List Is :",my_list)

    my_filter=list(filter(lambda x:x%2==0,my_list))
    print("List after filter :",my_filter)

    my_map=list(map(lambda x:x*x,my_filter))
    print("List after map :",my_map)

    my_reduce=reduce(lambda x,y:x+y,my_map)
    print("List after reduce :",my_reduce)


def main():
    
    

    fltr_map_reduce()


if __name__ == "__main__":
    main()