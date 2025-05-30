import multiprocessing.process
import threading
import multiprocessing
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

def Mul(no1,no2):
   
   mult=no1*no2
   print("Multiplication is :",mult)
   print("Process Id is :",os.getpid())

def Division(no1,no2):
   div=no1/no2
   print("Division is :",div)
   print("Process Id is :",os.getpid())

def main():
#  print("Process Id is :",os.getpid())
 
 p1=multiprocessing.Process(target=Add,args=(50,60))
 p1.start()
 start_time=time.time()
 
 p1.join()

 end_time=time.time()

 print("Time taken for addition is :",end_time-start_time)

 print()

 p2=multiprocessing.Process(target=Diff,args=(50,60))
 p2.start()
 start_time=time.time()
 p2.join()
 end_time=time.time()

 print("Time taken for Difference  is :",end_time-start_time)

 print()

 p3=multiprocessing.Process(target=Mul,args=(50,60))
 p3.start()
 start_time=time.time()
 p3.join()
 end_time=time.time()

 print("Time taken for Multiplication  is :",end_time-start_time)

 print()

 p4=multiprocessing.Process(target=Division,args=(50,60))
 p4.start()
 start_time=time.time()
 p4.join()
 end_time=time.time()

 print("Time taken for Division is :",end_time-start_time)


if __name__ =="__main__":
    main()