import time
import schedule
import datetime


def DoCoding():
    print("Do Coding--!")

def main():

    schedule.every(30).minutes.do(DoCoding)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()