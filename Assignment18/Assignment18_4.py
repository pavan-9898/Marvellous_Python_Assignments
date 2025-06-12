import os
import sys
import filecmp

def checkcontent(file1,file2):

    file1=os.path.exists(file1)
    file2=os.path.exists(file2)

    if file1 and file2==True:

        Filename1=open(str(sys.argv[1]),"r")
        data1=Filename1.read() # reading the file
        data1=data1.split() # here spliting the data so that we can get list
        # print(data1)  # printing the splited data here 
        Filename2=open(str(sys.argv[2]),"r")
        data2=Filename2.read() # reading the file
        data2=data2.split() # here spliting the data so that we can get list
        # print(data2) # printing the splited data here 

        if data1==data2:  # and finally here comparing 2 list 
            print("File content is same")
        else:
            print("File content is not same")
    else:
        print("File does not exist")



def main():

    file1=sys.argv[1]
    file2=sys.argv[2]

    checkcontent(file1,file2)


if __name__=="__main__":
    main()