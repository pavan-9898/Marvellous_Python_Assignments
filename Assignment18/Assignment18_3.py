import os
import sys
import shutil

def copyfile(FileName):

    flag=os.path.exists(FileName)

    if(flag==True):

        newfile=open("copied.txt","w")
        content=shutil.copyfile(str(FileName),"copied.txt")
        print("Data copied successfully")
    else:
        print("File does not exist")


def main():

    FileName=sys.argv[1]
    copyfile(FileName)


if __name__=="__main__":
    main()