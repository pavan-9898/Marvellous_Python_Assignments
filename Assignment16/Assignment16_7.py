def main():
    data=[]
    with open("marks.txt","r") as f:
        for line in f:
            col=line.strip().split(",")
            if len(col)>1:
                data.append(col[1])
        for i in data:
            if int(i)>=75:
                print(i)
                
    # print(data)
    # print(type(data))


if __name__ =="__main__":
    main() 