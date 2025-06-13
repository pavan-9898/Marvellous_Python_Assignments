import os
import sys

def RenameExtension(DirName,extension1,extension2):

    flag=os.path.isabs(DirName)

    if flag==False:
        DirName=os.path.abspath(DirName)
        print("Absolute path is :"+DirName)
    
    flag=os.path.exists(DirName)

    if flag==False:
        print("Path is invalid")
        exit()
    
    flag=os.path.isdir(DirName)

    if flag==False:
        print("Path is valid but target is not directory")
        exit()

    for FolderNames,SubFolderNames,FileNames in os.walk(DirName):

        # for foldername in FolderNames:
           for fname in FileNames:
               
               file=os.path.join(DirName,fname)
               print(file)
               os.rename(extension1,extension2)

            # os.path.join(FolderNames,fname)
           
            # os.rename(extension1,extension2)
    
def main():

    DirName=sys.argv[1]
    extension1=sys.argv[2]
    extension2=sys.argv[3]

    RenameExtension(DirName,extension1,extension2)


if __name__=="__main__":
    main()