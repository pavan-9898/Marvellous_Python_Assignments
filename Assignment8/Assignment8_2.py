import threading

def evenfactor(no):
    fact=1
    for i in range(2,no+1): 
        if i%2==0:
         fact=fact*i
         no=no-1
    print("Sum Of EvenFactor Number Is: ",fact)

def oddfactor(no):
  fact=1
  for i in range(1,no+1):
       if i%2!=0:
         fact=fact*i
         no=no-1
  print("Sum Of OddFactor Is : ",fact)


def main():

 T1=threading.Thread(target=evenfactor,args=(10,))
 T2=threading.Thread(target=oddfactor,args=(10,))

 T1.start()
 T2.start()

 T1.join()
 T2.join()

 print("Exit From Main.")

if __name__== "__main__":
    main()