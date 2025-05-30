def main():

    name="Hello World"
    print(len(name)) # 5
    print(name[2:4]) # ll
    print(name[::-1]) #olleh
    print(name.upper()) #HELLO
    print(name.lower()) #hello
    print(name.split(","))
    print(name.replace("World","pavan"))

    print()


    with open("my_file.txt","r") as file:
        content=file.read()          
        print(content)                                                                


     



if __name__ == "__main__":
    main()