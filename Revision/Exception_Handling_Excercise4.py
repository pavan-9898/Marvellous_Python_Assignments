def index_exception():

    try:
        num=[10,20,30,40,50]
        print(num[6])
    except IndexError as i:
        print("Index Error :",i)
    finally:
        print("Finally block executed")

def main():

    index_exception()


if __name__=="__main__":
    main()