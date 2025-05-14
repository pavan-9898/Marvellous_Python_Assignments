def display_star(no1):
 no2=0
 while no1>no2:
    print("*")
    no2=no2+1
    
def main():
   print("Enter number")
   no=int(input())
   display_star(no)

if __name__ =="__main__":
    main()