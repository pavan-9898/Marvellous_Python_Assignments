import psutil


def main():

    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=['name','pid','username'])
        
        print(info)


if __name__=="__main__":
    main()