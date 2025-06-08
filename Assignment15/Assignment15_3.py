import os
def main():

    print("Enter the file name that you want to copy the data from another file ")
    Filename=input()
    ret=os.path.exists(Filename)
    if(ret==True):
        #  open(Filename,"r")
         with open("Demo.txt","w") as demo:
             with open(Filename,"r") as r:
              for data in r:
                 demo.write(data)
         print("data copied successfully")
    
    else:
        print("File is not present")

# print("data copies successfully")


if __name__ =="__main__":
    main() 