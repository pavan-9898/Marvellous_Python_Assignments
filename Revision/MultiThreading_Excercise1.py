import threading

def gun():
    print("inside gun")

def add(no1,no2):
    sum=0
    sum=no1+no2
    print("addition is :",sum)

def main():

    t1=threading.Thread(target=gun)
    t1.start()
    t1.join()

    print("Thread name is :",threading.current_thread().name)
    t2=threading.Thread(target=add,args=(10,20))
    
    t2.start()
    t2.join()
    
    print("Thread name is :",threading.current_thread().name)


if __name__ == "__main__":
    main()