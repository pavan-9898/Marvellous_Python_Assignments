def main():

        fobj=open("Student.txt","w")
        fobj.write("sam")
        fobj.write("\npavan")
        fobj.write("\npritam")
        fobj.write("\npankaj")
        fobj.write("\nPranit")

        fobj=open("Student.txt","r")
        ret=fobj.read()
        print(ret)


if __name__ =="__main__":
    main() 