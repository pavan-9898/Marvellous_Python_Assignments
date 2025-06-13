import os
import sys
import shutil

def Copy_Files_From_One_Directory_To_Another(dir1,dir2,extension):

    flag=os.path.isabs(dir1)

    if flag==False:
        dir1=os.path.abspath(dir1)
        print("Absolute path is :"+dir1)
    
    flag=os.path.abspath(dir1)

    if flag==False:
        print("Path is invalid")
        exit()
    

    flag=os.path.isdir(dir1)

    if flag==False:
        print("Path is valid but target is not directory")
        exit()

    if os.path.exists(dir2):
        print("Directory Name already exist please check")
        exit()

    NewDir=os.mkdir(dir2)

    for FolderNames,SubFolder,FileNames in os.walk(dir1):
        
        for fname in FileNames:
            fname=os.path.join(str(dir1),fname)
            # print(fname)

            if extension in fname:
                # print(fname)
                shutil.copy2(str(fname),str(dir2))
        print("Files copied successfully")


def main():
   
   dir1=sys.argv[1]
   dir2=sys.argv[2]
   extension=sys.argv[3]

   Copy_Files_From_One_Directory_To_Another(dir1,dir2,extension)


if __name__=="__main__":
    main()