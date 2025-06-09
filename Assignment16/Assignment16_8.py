def main():

    # fobj=open("data.txt","r")
    # data=fobj.read()
    # ret=data.replace("\n\n","\n")
    # fobj=open("output.txt","w")
    # data=fobj.write(ret)
    # print("removed the lines")

    with open('data.txt', 'r') as f: 

     lines = f.readlines()
    #  print(lines)

    blanklines = [line for line in lines if line.strip()]
    # print(blanklines)

    with open('output.txt', 'w') as f:
     f.writelines(blanklines)

     print("Removed all blank lines")




if __name__ =="__main__": 
    main()