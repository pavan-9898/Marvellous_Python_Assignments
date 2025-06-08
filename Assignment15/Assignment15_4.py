import sys
def main():

    if len(sys.argv)>1:
        filename1=sys.argv[1]
        filename2=sys.argv[2]
        data1=open(filename1,"r")
        f1=data1.read()
        data2=open(filename2,"r")
        f2=data2.read()
        if f1 == f2:
            print("Success")
        else:
            print("Failure")


if __name__ =="__main__":
    main() 