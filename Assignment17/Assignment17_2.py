import schedule
import time
import datetime

def current_date_time():

    print("Current date and time is :",datetime.datetime.now())

def main():

    schedule.every(1).minute.do(current_date_time)

    while True:

        schedule.run_pending()
        time.sleep(1)


if __name__ =="__main__":
    main() 