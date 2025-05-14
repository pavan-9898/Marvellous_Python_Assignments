def lst_max(numbers_lst):

    if numbers_lst:
        max_num=max(numbers_lst)
        print("maximum is: ",max_num)
    else:
        print("List is Empty :")
    

def main():

    print("Enter the number of elements :")
    no=int(input())
    numbers_lst=[]
    for i in range(no):
        num=(int(input(f"Enter the {i+1} element :")))
        numbers_lst.append(num)
        lst_max(numbers_lst)

if __name__ == "__main__":
    main()