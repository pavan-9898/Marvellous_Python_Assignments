class Number:
   
#    def __init__(self,A):
#       self.num=A
    
    def CheckPerfect(self,num):
       sum=0
       for i in range(1,num):
          if num%i==0:
             sum=sum+i
       return sum==num
   

    def Factor(self,num):
      for i in range(1,num):
         if num%i==0:
            print(i)
        
    def Sum_Factor(self,num):
       sum=0
       for i in range(1,num):
          if num%i==0:
             sum=sum+i
       return sum
    

def main():

 obj=Number()
 ret=obj.CheckPerfect(6)
 print(ret)
 print()

 obj2=Number()
 obj2.Factor(6)

 print()

 obj3=Number()
 ret=obj3.Sum_Factor(6)
 print("sum of all factors is",ret)



if __name__ == "__main__":
    main()