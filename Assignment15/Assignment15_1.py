import os

def main():

    print("Enter file name that you want to check")
    FileName=input()

    ret=os.path.exists(FileName)
    if(ret==True):
        print("File is Present")
    else:
        print("File is not present")


if __name__ =="__main__":
    main() 