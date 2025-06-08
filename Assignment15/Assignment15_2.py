import os
def main():

    print("Enter file name that you want to display the data in it")
    FileName=input()
    ret=os.path.exists(FileName)
    if(ret==True):
        fobj=open(FileName,"r")
        data=fobj.read()
        print("The data is :",data)
        fobj.close()
    else:
        print("File is not present")


if __name__=="__main__":
    main()