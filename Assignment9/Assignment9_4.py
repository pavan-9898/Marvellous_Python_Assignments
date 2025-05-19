import time
import multiprocessing
import threading

def add():
    sum=0
    for i in range(1,10000000+1):
        sum=sum+i
    print(sum)
def main():

    start_time=time.time()
    add()
    end_time=time.time()

    print("Time took for normal function to add 1 to 10 million is :",end_time-start_time)
     
    start_time=time.time()
    T1=threading.Thread(target=add)
    
    T1.start()
    T1.join()

    end_time=time.time()
    print("Time took for using threading to add 1 to 10 million is :",end_time-start_time)

    
    p=multiprocessing.Process(target=add)
    p.start()
    start_time=time.time()
    p.join()
    end_time=time.time()
    print("Time took for using multiprocessing to add 1 to 10 million is :",end_time-start_time)

if __name__ == "__main__":
    main()