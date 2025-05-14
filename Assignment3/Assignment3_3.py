def lst_num(num_lst):
   if num_lst:
      minimum=min(num_lst)
      print("minimum Is :",minimum)

def main():

    print("Enter the number :")
    no=int(input())
    num_lst=[]
    for i in range(no):
     numbers=int(input(f"Enter the  {i+1} elements:"))
     num_lst.append(numbers)
     lst_num(num_lst)


if __name__ == "__main__":
    main()