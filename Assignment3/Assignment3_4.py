def lst_freq(num_lst):
   frequancy={}
   for item in num_lst:
      if item in frequancy:
         frequancy[item]+=1
      else:
         frequancy[item]=1
   print(frequancy)
   
def main():
    print("Enter the number :")
    no=int(input())
    num_lst=[]
    for i in range(no):
     numbers=int(input(f"Enter the  {i+1} elements:"))
     num_lst.append(numbers)
     no=int(input("Enter Element to search:"))
     lst_freq(num_lst)
     
     #print(num_lst)
    

if __name__ == "__main__":
    main()