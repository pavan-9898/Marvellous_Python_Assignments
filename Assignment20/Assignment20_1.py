import hashlib
import os 
import sys

def CheckSum(path):

    fobj=open(path,"rb")
    hobj=hashlib.md5()

    buffer=fobj.read(1024)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(1024)

        fobj.close()
    
    return hobj.hexdigest()


def DirectoryWatcher(DirName):

    flag=os.path.isabs(DirName)
    
    if flag==False:
        DirName=os.path.abspath(DirName)
    
    flag=os.path.exists(DirName)

    if flag==False:
        print("Invalid Path,Directory not found")
        exit()
    
    flag=os.path.isdir(DirName)

    if flag==False:
        print("Path is valid but target is not directory")
        exit()
    
    for FolderNames,SubFolderNames,FileNames in os.walk(DirName):
        for fname in FileNames:
            fname=os.path.join(DirName,fname)
            checksum=CheckSum(fname)
            print(f"Checksum of file {fname } is :",checksum)


def main():

    DirName=sys.argv[1]
    DirectoryWatcher(DirName)



if __name__=="__main__":
    main()