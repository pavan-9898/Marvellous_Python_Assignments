import os
import hashlib
import sys
import time

def CheckSum(path):

    fobj=open(path,"rb")
    hobj=hashlib.md5()

    buffer=fobj.read(1024)

    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(1024)

        fobj.close()
    
    return hobj.hexdigest()

def FindDuplicate(DirName="Demo"):

    flag=os.path.isabs(DirName)

    if flag==False:
        DirName=os.path.abspath(DirName)
    
    flag=os.path.exists(DirName)

    if flag==False:
        print("Path is invalid")
        exit()
    
    flag=os.path.isdir(DirName)

    if flag==False:
        print("Path is valid but target is not directory")
        exit()

    Duplicate={}
    
    for FolderNames,SubFolderNames,FileNames in os.walk(DirName):
        for fname in FileNames:
            fname=os.path.join(DirName,fname)
            checksum=CheckSum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum]=[fname]

    return Duplicate


def DirectoryWatcher(DirName):

    flag=os.path.isabs(DirName)

    if flag==False:
        DirName=os.path.abspath(DirName)
    
    flag=os.path.exists(DirName)

    if flag==False:
        print("Invalid path ,Directory not exist")
        exit()
    
    flag=os.path.isdir(DirName)

    if flag==False:
        print("path is valid but target is not directory")
        exit()

    for FolderNames,SubFolderNames,FileNames in os.walk(DirName):
        for fname in FileNames:
            fname=os.path.join(DirName,fname)
            checksum=CheckSum(fname)
            print(checksum)


def Createlog():
    timestamp=time.ctime()
    timestamp=timestamp.replace(" ","")
    timestamp=timestamp.replace(":","_")
    timestamp=timestamp.replace("/","_")

    # FileName= os.path.join(FolderName,"Marvellous%s.Log" %(timestamp))

    FileName="Log.txt" 

    fobj=open(FileName,"w")

    Border="-"*80
    fobj.write(Border)
    fobj.write("\n\t\tMarvellous Infosystems CheckSumDuplicate Log\n")
    fobj.write("\t\tLog file is created at :"+time.ctime()+"\n")
    fobj.write(Border)

    fobj.write("\nDuplicate file is :"+str(FindDuplicate().values())+"\n")
    
   

 
    

def DisplayResult(MyDict):
    result=list(filter(lambda x:len(x)>1,MyDict.values()))
    count=0
    for  value in result:
        for subvalue in value:
            count=count+1
            print(subvalue)
        print("----------------------------")
        print("value of count is :",count)
        print("-----------------------------")
        count=0       

def main():

    DirName=sys.argv[1]
    # DirectoryWatcher(DirName)
    result=FindDuplicate(sys.argv[1])
    DisplayResult(result)
    Createlog()



if __name__=="__main__":
    main()