import os

def checkfile(FileName):

    flag=os.path.exists(FileName)

    if flag==True:

        fobj=open(FileName,"r")
        data=fobj.read()
        print(data)
        fobj.close()
    else:
        print("File does not exist")

def main():

    print("Enter the file name that you want to oepn and read the content in it")
    FileName=input()
    checkfile(FileName)


if __name__=="__main__":
    main()