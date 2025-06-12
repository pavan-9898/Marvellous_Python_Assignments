import os
import sys

def searchstring(FileName,search):

    flag=os.path.exists(FileName)

    if flag==True:

        FileName=open(str(FileName),"r")
        data=FileName.read()
        data=data.split()
        # print(data)
        # print(type(data))

        count=0
 
        for i in data:
            
            if i==search:
                count+=1
        print("Number of frequency is :",count)
    else:
        print("File does not exist")



def main():

    print("Enter the file name")
    FileName=input()
    print("Enter the string that you want to search ")
    search=input()

    searchstring(FileName,search)


if __name__=="__main__":
    main()