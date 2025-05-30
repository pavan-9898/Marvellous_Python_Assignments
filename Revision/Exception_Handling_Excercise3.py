def file_exception():

    try:
        with open("MultiThreading_Excercis3.py","r") as file:
            content=file.read()
            print(content)

    except FileNotFoundError as F:
        print("File does not exists:",F)

    finally:
        print("Finally block executed")

def main():
    
    file_exception()


if __name__=="__main__":
    main()