import sys
def main():
    
    if len(sys.argv)>1:
        filename=sys.argv[1]
        search=sys.argv[2]

        fobj=open(filename,"r")
        data=fobj.read()

        if search in data:
            print("String is available")
        else:
            print("String is not available")

if __name__ =="__main__":
    main() 