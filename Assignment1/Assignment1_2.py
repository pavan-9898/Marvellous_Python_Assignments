def ChkNum(no1):
  
  if no1 %2==0:
    print("Even Number")
  else:
   print("Odd Number")
   #return no1

def main():
 print("enter number")
 number=int(input())
 ChkNum(number)
if __name__ == "__main__":
  main()