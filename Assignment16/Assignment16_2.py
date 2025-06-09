def main():

    fobj=open("data.txt","w")
    data=fobj.write("India Is My Country")
    fobj.close()
    fobj2=open("data.txt","r")
    data=fobj2.read()
    print("data in the file :",data)



if __name__ =="__main__":
    main() 