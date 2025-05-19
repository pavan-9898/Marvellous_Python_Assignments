import threading

def even(no):
    
    for i in range(2,no+1):
        if i%2==0:
            print("Even Numbers Are :",i)

        

def odd(no):
    for i in range(1,no+1):
        if i%2!=0:
            print("Odd Numbers Are :",i)


def main():

  T1=threading.Thread(target=even,args=(10,))
  T2=threading.Thread(target=odd,args=(10,))

  T1.start()
  T2.start()

  T1.join()
  T2.join()


if __name__=="__main__":
    main()