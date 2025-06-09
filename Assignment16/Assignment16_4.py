def main():
 
 numbers=[]

 for i in range(10):
    while True:
      num=int(input(f"Enter {i+1} number"))
      numbers.append(num)
      break


    fobj=open("number.txt","w")
    for num in numbers:
     fobj.write(str(num)+"\n")

 print("Numbers are written in file please check")

      

if __name__ =="__main__":
    main() 