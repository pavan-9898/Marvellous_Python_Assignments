import threading

def even():
    count=0
    for i in range(30,50):
        if i%2==0:
             count=count+1
    print("Total  even numbers is :",count)

def odd():
    count=0
    for i in range(30,50):
        if i%2!=0:
            count=count+1
    print("Total odd numbers is :",count)

def main():
    
    t1=threading.Thread(target=even)
    t1.start()
    t1.join()

    t2=threading.Thread(target=odd)
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()