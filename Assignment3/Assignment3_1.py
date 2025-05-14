def lst_sum(numbers):
        sum=0
        for i in numbers:
          sum=  sum+i
        print("Addition  Is :",sum)    
   
def main():
    
    
    print("Enter Number Of Elements:")
    no=int(input())
    numbers=[]  # Initializing Empty list
    for i in range(no):
        num=int(input(f"Enter the {i+1} element :"))
        numbers.append(num) # Appeding the numbers into the list
    lst_sum(numbers) # calling funtion with list

if __name__ == "__main__":
    main()