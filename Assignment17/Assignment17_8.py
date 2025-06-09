import time
import datetime
import schedule


def EmailChecking():
    print("Cheking the Emails")

def main():

    schedule.every(10).seconds.do(EmailChecking)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()