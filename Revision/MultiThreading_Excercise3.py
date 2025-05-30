import threading
import time
import os

def Add(no1,no2):
   sum=0
   sum=no1+no2
   print("Addition is :",sum)
   print("Process Id is :",os.getpid())

def Diff(no1,no2):
   diff=0
   diff=no1-no2
   print("Difference is :",diff)
   print("Process Id is :",os.getpid())

def Multi(no1,no2):
   
   mult=no1*no2
   print("Multiplication is :",mult)
   print("Process Id is :",os.getpid())

def Division(no1,no2):
   div=no1/no2
   print("Division is :",div)
   print("Process Id is :",os.getpid())

def main():
 
#  print("Process Id is :",os.getpid())
 
 t1=threading.Thread(target=Add,args=(50,60))
 t1.start()
 start_time=time.time()
 
 t1.join()

 end_time=time.time()

 print("Time taken for addition is :",end_time-start_time)

 print()

 t2=threading.Thread(target=Diff,args=(50,60))
 t2.start()
 start_time=time.time()
 t2.join()
 end_time=time.time()

 print("Time taken for Difference  is :",end_time-start_time)

 print()

 t3=threading.Thread(target=Multi,args=(50,60))
 t3.start()
 start_time=time.time()
 t3.join()
 end_time=time.time()

 print("Time taken for Multiplication  is :",end_time-start_time)

 print()

 t4=threading.Thread(target=Division,args=(50,60))
 t4.start()
 start_time=time.time()
 t4.join()
 end_time=time.time()

 print("Time taken for Division is :",end_time-start_time)


if __name__ =="__main__":
    main()