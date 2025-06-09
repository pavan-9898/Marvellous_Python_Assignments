import schedule
import time
import datetime

def Namskar():
    print("Namskar")

def main():

    schedule.every(1).day.at("21:00").do(Namskar)  # time given in 24 hrs format 

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ =="__main__":
    main()