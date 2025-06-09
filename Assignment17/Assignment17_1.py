import schedule
import time
import datetime
# import os

def JayGanesh():
        print("Current time is :",datetime.datetime.now())
        print("Jay Ganesh")

def main():
       
       print("Current time is :",datetime.datetime.now())
       
       schedule.every(2).seconds.do(JayGanesh)

       while True:
             schedule.run_pending()
             time.sleep(1)

 


if __name__ == "__main__":
    main() 