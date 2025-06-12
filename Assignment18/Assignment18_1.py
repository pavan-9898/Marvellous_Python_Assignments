import os

def checkfile(FileName):

    flag=os.path.exists(FileName)

    if flag==True:
        print("File is exist")
    else:
        print("File is not exist")

def main():

    print("Enter File Name that you want to check")
    FileName=input()
    checkfile(FileName)

if __name__=="__main__":
    main()