def main():

    fobj=open("data.txt","r")
    data=fobj.readlines()
    print(data)
    print("Number of lines in file are :",len(data))

if __name__ == "__main__":
    main() 