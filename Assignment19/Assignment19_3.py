import os
import sys
import shutil

def Copy_All_Data_From_One_Directory_To_New_Directory(dir1,dir2):

    flag=os.path.isabs(dir1)

    if flag==False:
        dir1=os.path.abspath(dir1)
        print("Absolute path is :"+dir1)
    
    flag=os.path.abspath(dir1)

    if flag==False:
        print("Path is Invalid")
        exit()
    
    flag=os.path.isdir(dir1)

    if flag==False:
        print("Path is correct but target is not directory")
        exit()
    
    if os.path.isdir(dir2): # checking if the new directory name already exist or not
        print("Directory Name already exist please check")
        exit()


    NewDir=os.mkdir(dir2)  # creates new directory
    
    for FolderNames,SubFolderNames,FileNames in os.walk(dir1):

        for fname in FileNames:
            # print(fname)
            fname=os.path.join(str(dir1),fname)
            shutil.copy2(str(fname),str(dir2)) # copying files to new directory
        print("Data copied successfully")


def main():

    dir1=sys.argv[1] # accepting 1st dir name from command line and stroring it into dir1
    dir2=sys.argv[2] # accepting 2nd dir name from command line and stroring it into dir2 
    Copy_All_Data_From_One_Directory_To_New_Directory(dir1,dir2) # calling the function


if __name__ =="__main__":
    main()