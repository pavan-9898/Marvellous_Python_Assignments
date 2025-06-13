import os
import sys

def Files_With_Extensions(Dirname,extension):

    flag=os.path.isabs(Dirname)

    if flag==False:
        Dirname=os.path.abspath(Dirname)
        print("Absolute path is :"+Dirname)
    
    print()

    print(f"List of file with {extension}")

    flag=os.path.exists(Dirname)

    if flag==False:
            print("Path is valid but target is not a directory")
            exit()
        
    for FolderNames,SubFolderNames,FileNames in os.walk(Dirname):
         
         for file in FileNames:

              if extension in file: # we got the string i.e.in file and we are checking using in operator 
                                    #i.e extension is exist in string(file) or not
                   print(file)

def main():

    Dirname=sys.argv[1]
    extension=sys.argv[2]
    Files_With_Extensions(Dirname,extension)


if __name__=="__main__":
    main()