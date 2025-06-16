import psutil
import sys

def main():

    # print("Enter the process name")
    # pname=input() # python.exe

    pname=sys.argv[1] # python.exe

    for proc in psutil.process_iter(['name','pid']):
        if proc.info['name']==pname:
            print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")
        



if __name__=="__main__":
    main()