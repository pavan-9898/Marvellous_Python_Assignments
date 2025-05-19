import threading

def Even_list(evn_list):
    sum=0
    for i in evn_list:
        if i%2==0:
            sum=sum+i
    print("Sum of even list is : ",sum)

def Odd_list(odd_list):
    sum=0
    for i in odd_list:
        if i%2!=0:
         sum=sum+i
    print("Sum of Odd list is :",sum)

def main():

    evenlist=threading.Thread(target=Even_list,args=([1,2,3,4,5,6,7,8,9,10],))
    evenlist.start()
    evenlist.join()

    oddlist=threading.Thread(target=Odd_list,args=([1,2,3,4,5,6,7,8,9,10],))
    oddlist.start()
    oddlist.join()
    print("Exit From Main.")


if __name__ == "__main__":
    main()