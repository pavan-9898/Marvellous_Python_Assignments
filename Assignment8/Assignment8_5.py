import threading
import time

def Display1():
    for i in range(1,51):
        print(i)

    
def Display2():
    for i in range(50,0,-1):
        print(i)
    

def main():
    start_time=time.time()
    thread1=threading.Thread(target=Display1)
    thread1.start()
    thread1.join()

    end_time=time.time()

    total_time=end_time-start_time

    print("Execution time required for thread1 is :",total_time)

    start_time=time.time()
    thread2=threading.Thread(target=Display2)
    
    time.sleep(total_time)
    print("Started thread 2 now ")
    thread2.start()
    
    thread2.join()

    end_time=time.time()

    print("Execution time required for thread2 is :",end_time-start_time)
    

if __name__ == "__main__":
    main()
    